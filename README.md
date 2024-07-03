# Pythoninmymind - сайт о программировании на python
Мой сайт о программировании на python, статьи в который я пишу сам. 
Главной его фишкой является конвертация markdown текста в HTML. При добавлении статьи в админ панели вставляется  Поддерживается весь основной синтаксис markdown, а также добавлен функционал коротких ссылок на статьи на сайте вида `[slug:<слаг статьи>]`.
Реализована подсветка кода. Чтобы подсветка работала, необходимо указать название языка сразу после тройного апострофа.

У сайта имеются следующие страницы:

- `/` - главная страница
- `/all_articles` - все статьи на сайте, также настроен пагинатор.
- `/search` - поиск по тексту и заголовку статей. 
- `/articles/<str:slug>` - конкретная статья.
- `/sitemap.xml` - файл sitemap, предназначенный для индексации страниц сайта поисковыми системами.