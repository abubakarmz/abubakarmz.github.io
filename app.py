from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на ваш собственный секретный ключ

@app.route('/')
def index():
    interests = [
        {"name": "Спорт", "image": "interest1.png"},
        {"name": "Творчество", "image": "interest2.png"},
        {"name": "Наука", "image": "interest3.png"},
        {"name": "Музыка", "image": "interest4.png"},
        {"name": "Технологии", "image": "interest5.png"},
        {"name": "Игры", "image": "interest6.png"}
    ]
    return render_template('index.html', interests=interests)


# Заглушки для других маршрутов
@app.route('/create_profile')
def create_profile():
    flash("Страница создания профиля будет доступна в будущем.", "info")
    return redirect(url_for('index'))

@app.route('/search_events')
def search_events():
    flash("Страница поиска мероприятий будет доступна в будущем.", "info")
    return redirect(url_for('index'))

@app.route('/book_event')
def book_event():
    flash("Страница бронирования мероприятий будет доступна в будущем.", "info")
    return redirect(url_for('index'))

@app.route('/rate_event')
def rate_event():
    flash("Страница оценки мероприятий будет доступна в будущем.", "info")
    return redirect(url_for('index'))

@app.route('/calendar_integration')
def calendar_integration():
    flash("Интеграция с календарями будет доступна в будущем.", "info")
    return redirect(url_for('index'))

@app.route('/notifications')
def notifications():
    flash("Настройка уведомлений будет доступна в будущем.", "info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
