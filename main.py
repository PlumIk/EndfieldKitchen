from enum import Enum

class DishQuality(Enum):
    CHARMING = "Прелестное"
    EXQUISITE = "Изысканное"
    VEGETABLE = "Овощное"
    SPICY_AROMATIC = "Прянное"
    WITH_WATERFOWL = "С водоплавом"
    SALTY = "Соленое"
    HEARTY = "Сытное"
    SOUR = "Кислое"
    SWEET = "Сладкое"
    MEAT = "Мясное"
    HOT_SPICY = "Острое"
    NOTHING = "Ничего"

class DishType(Enum):
    SIDE_DISH = "Гарнир"
    SOUP = "Суп"
    MAIN_COURSE = "Основное блюдо"
    DESSERT = "Десерт"
    CHEF_SPECIAL = "От шефа"

class Worker:
    def __init__(self, name: str, type1: DishType, type2: DishType, quality: DishQuality):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.quality = quality
        
class Dish:
    def __init__(self, name: str, quality1: DishQuality, quality2: DishQuality, dish_type: DishType, cooking_time: int, price: int):
        self.name = name
        self.quality1 = quality1
        self.quality2 = quality2
        self.dish_type = dish_type
        self.cooking_time = cooking_time
        self.price = price


DISHES_LIST = [
    # Супы
    Dish("Суп с цветами тофу", DishQuality.CHARMING, DishQuality.EXQUISITE, DishType.SOUP, 40, 120),
    Dish("Суп снежный гриб и лотос", DishQuality.VEGETABLE, DishQuality.EXQUISITE, DishType.SOUP, 40, 110),
    Dish("Белый бульон из водоплава", DishQuality.SPICY_AROMATIC, DishQuality.WITH_WATERFOWL, DishType.SOUP, 40, 105),
    Dish("Грибной крем-суп", DishQuality.SALTY, DishQuality.VEGETABLE, DishType.SOUP, 40, 100),
    Dish("Суп с белотыквой и фрикадельками", DishQuality.SPICY_AROMATIC, DishQuality.HEARTY, DishType.SOUP, 40, 90),
    Dish("Уха из водоплава с томатинкой", DishQuality.SOUR, DishQuality.WITH_WATERFOWL, DishType.SOUP, 40, 90),
    Dish("Сладкие ягодные кусочки", DishQuality.SWEET, DishQuality.HEARTY, DishType.SOUP, 40, 70),
    Dish("Кисло-острый суп", DishQuality.HOT_SPICY, DishQuality.SOUR, DishType.SOUP, 40, 60),

    # Десерты
    Dish("Чизкейк с красными цветами", DishQuality.SOUR, DishQuality.CHARMING, DishType.DESSERT, 35, 125),
    Dish("Фруктовый жемчуг", DishQuality.SWEET, DishQuality.HEARTY, DishType.DESSERT, 35, 100),
    Dish("Снежный лунный пряник", DishQuality.SALTY, DishQuality.EXQUISITE, DishType.DESSERT, 35, 90),
    Dish("Золотой шифон", DishQuality.SALTY, DishQuality.MEAT, DishType.DESSERT, 35, 80),
    Dish("Лед со сладкими бобами", DishQuality.SWEET, DishQuality.NOTHING, DishType.DESSERT, 25, 60),
    Dish("Пудинг из кислянки", DishQuality.SOUR, DishQuality.NOTHING, DishType.DESSERT, 25, 55),
    Dish("Танъюфнь с бобовой пастой", DishQuality.SWEET, DishQuality.NOTHING, DishType.DESSERT, 25, 50),
    Dish("Солёные сырные крекеры", DishQuality.SALTY, DishQuality.NOTHING, DishType.DESSERT, 15, 36),
    Dish("Флан на пару", DishQuality.NOTHING, DishQuality.NOTHING, DishType.DESSERT, 15, 32),
    Dish("Клейкое рисовое пирожное", DishQuality.NOTHING, DishQuality.NOTHING, DishType.DESSERT, 15, 30),

    # Основные блюда
    Dish("Рулетки пограничный лун", DishQuality.MEAT, DishQuality.CHARMING, DishType.MAIN_COURSE, 35, 125),
    Dish("Чаошоу в остром соусе", DishQuality.SALTY, DishQuality.HOT_SPICY, DishType.MAIN_COURSE, 35, 100),
    Dish("Рулетик Суперводоплав", DishQuality.SOUR, DishQuality.SPICY_AROMATIC, DishType.MAIN_COURSE, 35, 85),
    Dish("Рис Восемь сокровищ", DishQuality.SWEET, DishQuality.CHARMING, DishType.MAIN_COURSE, 35, 80),
    Dish("Лапша с бобовым соусом", DishQuality.HOT_SPICY, DishQuality.NOTHING, DishType.MAIN_COURSE, 25, 60),
    Dish("Цзяоцзы с водоплавом", DishQuality.SPICY_AROMATIC, DishQuality.NOTHING, DishType.MAIN_COURSE, 25, 55),
    Dish("Мясной плов", DishQuality.SALTY, DishQuality.NOTHING, DishType.MAIN_COURSE, 25, 50),
    Dish("Тонизирующий конджи с зеленью", DishQuality.NOTHING, DishQuality.NOTHING, DishType.MAIN_COURSE, 15, 36),
    Dish("ЦзяоЦзы с грибами", DishQuality.NOTHING, DishQuality.NOTHING, DishType.MAIN_COURSE, 15, 32),
    Dish("Рис с овощами Юаньюань", DishQuality.NOTHING, DishQuality.NOTHING, DishType.MAIN_COURSE, 15, 28),
    Dish("Лапша ручной лепки", DishQuality.NOTHING, DishQuality.NOTHING, DishType.MAIN_COURSE, 15, 12),
    Dish("Баоцзы с мясом", DishQuality.NOTHING, DishQuality.NOTHING, DishType.MAIN_COURSE, 15, 12),

    # Гарниры
    Dish("Кисло-сладкий слиток из водоплава", DishQuality.EXQUISITE, DishQuality.WITH_WATERFOWL, DishType.SIDE_DISH, 35,115),
    Dish("Бессмертное изобилие удачи", DishQuality.SPICY_AROMATIC, DishQuality.HEARTY, DishType.SIDE_DISH, 35, 110),
    Dish("Пловец в ложке", DishQuality.SPICY_AROMATIC, DishQuality.SWEET, DishType.SIDE_DISH, 35, 90),
    Dish("Мясо сянго", DishQuality.HOT_SPICY, DishQuality.SALTY, DishType.SIDE_DISH, 35, 85),
    Dish("Мясо в горшочке", DishQuality.SWEET, DishQuality.MEAT, DishType.SIDE_DISH, 35, 85),
    Dish("Фруктово-ягодный салат", DishQuality.SOUR, DishQuality.VEGETABLE, DishType.SIDE_DISH, 35, 80),
    Dish("Шашлык на гриле", DishQuality.HOT_SPICY, DishQuality.NOTHING, DishType.SIDE_DISH, 25, 60),
    Dish("Жареные клубни", DishQuality.SALTY, DishQuality.NOTHING, DishType.SIDE_DISH, 25, 55),
    Dish("Водоплав с маринованной зеленью", DishQuality.SOUR, DishQuality.NOTHING, DishType.SIDE_DISH, 25, 55),
    Dish("Пикантные кусочки водоплава", DishQuality.SWEET, DishQuality.NOTHING, DishType.SIDE_DISH, 15, 36),
    Dish("Белотыква в соусе", DishQuality.NOTHING, DishQuality.NOTHING, DishType.SIDE_DISH, 15, 32),
    Dish("Жареный водоплав", DishQuality.NOTHING, DishQuality.NOTHING, DishType.SIDE_DISH, 15, 28),
    Dish("Измельчённые клубни с перцем", DishQuality.NOTHING, DishQuality.NOTHING, DishType.SIDE_DISH, 15, 12),
    Dish("Яйцо с томатинкой", DishQuality.NOTHING, DishQuality.NOTHING, DishType.SIDE_DISH, 15, 12),
]

WORKERS_LIST = [
    # Сладкое
    Worker("Перлика", DishType.SIDE_DISH, DishType.CHEF_SPECIAL, DishQuality.SWEET),
    Worker("Лино", DishType.SIDE_DISH, DishType.CHEF_SPECIAL, DishQuality.SWEET),
    Worker("Арклайт", DishType.MAIN_COURSE, DishType.SOUP, DishQuality.SWEET),
    Worker("Авивенна", DishType.SIDE_DISH, DishType.DESSERT, DishQuality.SWEET),
    Worker("Чжуан Фанъи", DishType.MAIN_COURSE, DishType.SOUP, DishQuality.SWEET),
    Worker("Антал", DishType.CHEF_SPECIAL, DishType.CHEF_SPECIAL, DishQuality.SWEET),

    # Соленое
    Worker("Чэнь Цяньюй", DishType.MAIN_COURSE, DishType.SOUP, DishQuality.SALTY),
    Worker("Лифэн", DishType.MAIN_COURSE, DishType.SOUP, DishQuality.SALTY),
    Worker("Да Пан", DishType.MAIN_COURSE, DishType.SIDE_DISH, DishQuality.SALTY),
    Worker("Кэтчер", DishType.MAIN_COURSE, DishType.SIDE_DISH, DishQuality.SALTY),
    Worker("Пограничник", DishType.SOUP, DishType.CHEF_SPECIAL, DishQuality.SALTY),
    Worker("Муррчена", DishType.MAIN_COURSE, DishType.SIDE_DISH, DishQuality.SALTY),

    # Кислое
    Worker("Гилберта", DishType.SOUP, DishType.DESSERT, DishQuality.SOUR),
    Worker("Арделия", DishType.SIDE_DISH, DishType.SOUP, DishQuality.SOUR),
    Worker("Тифея/Тифон", DishType.SIDE_DISH, DishType.SOUP, DishQuality.SOUR),
    Worker("Флюорит", DishType.SOUP, DishType.CHEF_SPECIAL, DishQuality.SOUR),

    # Острое
    Worker("Эмбер/Имбирь", DishType.MAIN_COURSE, DishType.DESSERT, DishQuality.HOT_SPICY),
    Worker("Лэватейн/Сургут", DishType.SIDE_DISH, DishType.CHEF_SPECIAL, DishQuality.HOT_SPICY),
    Worker("Акэкури", DishType.MAIN_COURSE, DishType.MAIN_COURSE, DishQuality.HOT_SPICY),
    Worker("Камиль", DishType.DESSERT, DishType.CHEF_SPECIAL, DishQuality.HOT_SPICY),
    Worker("Вульфгард", DishType.SOUP, DishType.CHEF_SPECIAL, DishQuality.HOT_SPICY),

    # Пряное
    Worker("Светоснежка", DishType.MAIN_COURSE, DishType.MAIN_COURSE, DishQuality.SPICY_AROMATIC),
    Worker("Ивонна", DishType.DESSERT, DishType.DESSERT, DishQuality.SPICY_AROMATIC),
    Worker("Эстелла", DishType.SIDE_DISH, DishType.CHEF_SPECIAL, DishQuality.SPICY_AROMATIC),
    Worker("Алеш", DishType.MAIN_COURSE, DishType.SOUP, DishQuality.SPICY_AROMATIC),
    Worker("Сайхи", DishType.DESSERT, DishType.CHEF_SPECIAL, DishQuality.SPICY_AROMATIC),
]

CHEF_SPECIAL_PRICE_MULTIPLAYER = 0.1
DEFAULT_CHEF_CHANCE = 0.03

THEME = [
    DishQuality.SPICY_AROMATIC,
    DishType.SOUP,
]


def suggest_best():
    all_dishes = DISHES_LIST

    selected_workers_list = WORKERS_LIST[:min(len(WORKERS_LIST), 6)]

    kitchens = []
    for i in range(0, min(len(selected_workers_list), 6), 2):
        kitchen_workers_list = selected_workers_list[i:i + 2]
        kitchens.append(kitchen_workers_list)

    while len(kitchens) < 3:
        kitchens.append([])

    result = {
        'kitchens': []
    }

    # Для отслеживания использованных блюд (чтобы не повторялись)
    used_dish_names = set()

    for kitchen_idx, kitchen_workers_list in enumerate(kitchens):
        suitable_dishes_list = []

        for dish in all_dishes:
            # Пропускаем блюдо, если оно уже выбрано для другой кухни
            if dish.name in used_dish_names:
                continue

            if kitchen_workers_list:
                suitable = False
                for worker in kitchen_workers_list:
                    if dish.dish_type == worker.type1 or dish.dish_type == worker.type2:
                        suitable = True
                        break

                if not suitable:
                    continue

            cooking_time = dish.cooking_time
            base_price = dish.price

            # Проверяем тему для бонуса цены
            theme_bonus = 0
            if matches_theme(dish, THEME):
                theme_matches = count_theme_matches(dish, THEME)
                theme_bonus = base_price * 0.1 * theme_matches

            chef_chance = DEFAULT_CHEF_CHANCE

            if kitchen_workers_list:
                time_discount = 0

                for worker in kitchen_workers_list:
                    # Проверяем совпадение типа для этого работника
                    type_match = (dish.dish_type == worker.type1 or dish.dish_type == worker.type2)
                    if type_match:
                        time_discount += 0.1

                    # Проверяем совпадение качества для этого работника
                    quality_match = (dish.quality1 == worker.quality or
                                     dish.quality2 == worker.quality)

                    if quality_match:
                        time_discount += 0.05
                        chef_chance += 0.05

                    # Проверяем, является ли этот работник шефом
                    if worker.type1 == DishType.CHEF_SPECIAL:
                        chef_chance += 0.05
                    if worker.type2 == DishType.CHEF_SPECIAL:
                        chef_chance += 0.05

                cooking_time *= (1 - time_discount)

            # Бонус от шефа = базовая цена * шанс * модификатор
            chef_bonus = base_price * chef_chance * CHEF_SPECIAL_PRICE_MULTIPLAYER

            final_price = base_price + theme_bonus + chef_bonus

            suitable_dishes_list.append({
                'dish': dish,
                'base_price': base_price,
                'cooking_time': cooking_time,
                'price': final_price,
                'score': final_price / cooking_time if cooking_time > 0 else 0,
                'chef_chance': chef_chance
            })

        suitable_dishes_list.sort(key=lambda x: x['score'], reverse=True)

        # Берем лучшее блюдо для этой кухни (топ-1, чтобы избежать повторов в рамках логики выбора)
        # Или можно топ-3, но тогда нужно проверять уникальность внутри кухни тоже
        top_dishes = suitable_dishes_list[:3]

        kitchen_info = {
            'kitchen_number': kitchen_idx + 1,
            'WORKERS_LIST': [w.name for w in kitchen_workers_list],
            'top_DISHES_LIST': []
        }

        for dish_info in top_dishes:
            # Добавляем имя блюда в использованные
            used_dish_names.add(dish_info['dish'].name)

            kitchen_info['top_DISHES_LIST'].append({
                'name': dish_info['dish'].name,
                'type': dish_info['dish'].dish_type.value,
                'qualities': [q.value for q in [dish_info['dish'].quality1, dish_info['dish'].quality2] if
                              q != DishQuality.NOTHING],
                'base_price': round(dish_info['base_price'], 2),
                'cooking_time': round(dish_info['cooking_time'], 1),
                'price': round(dish_info['price'], 2),
                'chef_chance': dish_info['chef_chance']
            })

        result['kitchens'].append(kitchen_info)

    return result


def count_theme_matches(dish, theme_tags):
    """Считает количество совпадений блюда с темой"""
    matches = 0
    for tag in theme_tags:
        if isinstance(tag, DishQuality):
            if dish.quality1 == tag:
                matches += 1
            if dish.quality2 == tag:
                matches += 1
        elif isinstance(tag, DishType):
            if dish.dish_type == tag:
                matches += 1
    return matches

def matches_theme(dish, theme_tags):
    """Проверяет, соответствует ли блюдо теме"""
    for tag in theme_tags:
        if isinstance(tag, DishQuality):
            if dish.quality1 == tag or dish.quality2 == tag:
                return True
        elif isinstance(tag, DishType):
            if dish.dish_type == tag:
                return True
    return False


def print_kitchens(result):
    if not result:
        print("Нет подходящих комбинаций")
        return

    for kitchen in result['kitchens']:
        print(f"Кухня {kitchen['kitchen_number']}:")

        if kitchen['WORKERS_LIST']:
            print(f"  Повара:")
            for worker_name in kitchen['WORKERS_LIST']:
                worker = next((w for w in WORKERS_LIST if w.name == worker_name), None)
                if worker:
                    types = f"{worker.type1.value}, {worker.type2.value}"
                    quality = worker.quality.value if worker.quality != DishQuality.NOTHING else "Нет"
                    print(f"    - {worker_name} (Типы: {types}, Качество: {quality})")
        else:
            print(f"  Повара: Нет")

        print(f"  Блюда:")

        for i, dish in enumerate(kitchen['top_DISHES_LIST'], 1):
            qualities_str = ', '.join(dish['qualities']) if dish['qualities'] else 'Нет'
            price_per_second = round(dish['price'] / dish['cooking_time'], 2)
            chef_mark = f" (Шанс шефа: {round(dish['chef_chance'] * 100, 1)}%)"
            print(f"    {i}. {dish['name']} ({dish['type']})")
            print(f"       Качества: {qualities_str}")
            print(
                f"       Базовая цена: {dish['base_price']}, Итоговая цена: {dish['price']}, Время: {dish['cooking_time']} сек, Цена/время: {price_per_second}{chef_mark}")

        print()

if __name__ == '__main__':
    print_kitchens(suggest_best())

