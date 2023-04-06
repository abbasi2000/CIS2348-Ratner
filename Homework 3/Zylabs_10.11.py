# 2095022
# #EMAD ABBASI
class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


def main():
    food_name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    num_serv = float(input())

    default_food_item = FoodItem()
    user_food_item = FoodItem(food_name, fat, carbs, protein)

    default_food_item.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'.format(num_serv, default_food_item.get_calories(num_serv)))

    user_food_item.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_serv, user_food_item.get_calories(num_serv)))


if __name__ == "__main__":
    main()
