from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# Функция расчета стоимости апгрейда
def get_upgrade_cost(upgrades):
    return 50 * (upgrades + 1) + 10 * upgrades

@app.route('/', methods=['GET', 'POST'])
def index():
    # 1. Читаем текущие данные из кук (если их нет, ставим 0)
    clicks = int(request.cookies.get('clicks', 0))
    upgrades = int(request.cookies.get('upgrades', 0))
    error_msg = ""

    # 2. Обрабатываем действия пользователя
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'click':
            clicks += 1 + upgrades

        elif action == 'upgrade':
            cost = get_upgrade_cost(upgrades)
            if clicks >= cost:
                clicks -= cost
                upgrades += 1
            else:
                error_msg = "Недостаточно кликов"

    # 3. Формируем ответ и сохраняем обновленные данные обратно в куки
    cost = get_upgrade_cost(upgrades)
    response = make_response(render_template('index.html', clicks=clicks, cost=cost, error_msg=error_msg))
    
    response.set_cookie('clicks', str(clicks))
    response.set_cookie('upgrades', str(upgrades))
    
    return response

if __name__ == '__main__':
    app.run(debug=True)