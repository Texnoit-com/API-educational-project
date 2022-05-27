from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Жанр',
                             help_text='Укажите жанр')
    slug = models.SlugField(max_length=255,
                            unique=True,
                            verbose_name='Параметр',
                            help_text='Адрес')
    description = models.TextField(verbose_name='Содержание',
                                   help_text='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста',
                            help_text='Введите текст поста')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    image = models.ImageField(verbose_name='Картинка',
                              upload_to='posts/',
                              blank=True,
                              help_text='Картинка')
    group = models.ForeignKey('Group',
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              verbose_name='Группа',
                              related_name="posts",
                              help_text='Группа, относительно поста')

    def __str__(self):
        return self.text

    class Meta:
        #ordering = ('-pub_date', 'author')
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             verbose_name='Текст поста',
                             related_name='comments',
                             blank=True,
                             null=True)
    text = models.TextField(verbose_name='Комментарий',
                            help_text='Напишите комментарий')
    created = models.DateTimeField(verbose_name='Дата добавления',
                                   auto_now_add=True,
                                   db_index=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='follower',
                             verbose_name='Подписчик')
    following = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='following',
                                  verbose_name='Подписка')

    def __str__(self):
        return f'{self.user} follows {self.following}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [models.UniqueConstraint(fields=['user', 'following'],
                                               name='unique_follow')]
