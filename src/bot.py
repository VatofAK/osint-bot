# Пример упрощенной логики внутри бота
def handle_phone_search(query):
    # 1. Получаем базовые данные по номеру
    base_data = get_phone_info(query) # Например: "Иван Иванов, Москва"
    
    # 2. Извлекаем ФИО из результата (автоматически)
    full_name = base_data['owner_name']
    
    # 3. Запускаем цепочку: ищем соцсети по полученному ФИО
    socials = get_social_media(full_name)
    
    # 4. Собираем всё в один красивый отчет
    report = f"📞 Номер: {query}\n👤 Владелец: {full_name}\n📍 Город: {base_data['city']}\n🌐 Соцсети: {socials}"
    return report

def handle_car_search(query):
    # 1. Получаем данные авто
    car_info = get_car_details(query) # Например: "BMW X5, Черный"
    
    # 2. Извлекаем владельца
    owner = car_info['owner_name']
    
    # 3. Добавляем информацию о владельце (через Aliens_eye или Master-OSINT)
    extra_details = get_deep_context(owner)
    
    return f"🚗 Авто: {car_info['brand']} {car_info['model']}\n👤 Владелец: {owner}\n✨ Доп. инфо: {extra_details}"

