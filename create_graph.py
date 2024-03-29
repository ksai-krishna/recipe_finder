class IngredientNode:
    def __init__(self, name):
        self.name = name
        self.recipes = []

class RecipeNode:
    def __init__(self, name):
        self.name = name
        self.ingredients = []


class RecipeGraph:
    def __init__(self):
        self.ingredients = {}  # Ingredient name to IngredientNode mapping
        self.recipes = {}      # Recipe name to RecipeNode mapping

    def add_recipe(self, recipe_name, ingredients, dish_type=None):  # Modified to accept dish_type
        recipe_node = RecipeNode(recipe_name)
        recipe_node.dish_type = dish_type  # Set the dish_type attribute
        self.recipes[recipe_name] = recipe_node
        
        for ingredient_name in ingredients:
            if ingredient_name not in self.ingredients:
                ingredient_node = IngredientNode(ingredient_name)
                self.ingredients[ingredient_name] = ingredient_node
            else:
                ingredient_node = self.ingredients[ingredient_name]
            ingredient_node.recipes.append(recipe_node)
            recipe_node.ingredients.append(ingredient_node)

def create_recipe_graph():
    recipe_graph = RecipeGraph()    
    recipe_graph.add_recipe("Pasta without sauce", ["Pasta", "Tomato Sauce"], dish_type="lunch food")
    recipe_graph.add_recipe("Raw Pasta", ["Pasta"], dish_type="lunch food")
    recipe_graph.add_recipe("Pasta", ["Pasta", "Tomato Sauce", "Cheese"], dish_type="lunch food")
    recipe_graph.add_recipe("Butter Chicken", ["Chicken", "Butter", "Tomato", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Paneer Tikka Masala", ["Paneer", "Tomato", "Cream", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Dal Makhani", ["Black Lentils", "Kidney Beans", "Butter", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Chole Bhature", ["Chickpeas", "Flour", "Yogurt", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Aloo Gobi", ["Potato", "Cauliflower", "Tomato", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Biryani", ["Basmati Rice", "Chicken", "Spices", "Yogurt", "Onion", "Tomato", "Mint", "Coriander"], dish_type="dinner food")
    recipe_graph.add_recipe("Samosa", ["Potato", "Peas", "Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Rasgulla", ["Milk", "Sugar", "Lemon Juice"], dish_type="sweet")
    recipe_graph.add_recipe("Gulab Jamun", ["Milk Powder", "Flour", "Sugar", "Cardamom"], dish_type="sweet")
    recipe_graph.add_recipe("Pani Puri", ["Semolina", "Potato", "Chickpeas", "Tamarind", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Jalebi", ["Flour", "Yogurt", "Sugar", "Saffron"], dish_type="sweet")
    recipe_graph.add_recipe("Chicken Tikka", ["Chicken", "Yogurt", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Pav Bhaji", ["Potato", "Tomato", "Onion", "Peas", "Capsicum", "Spices", "Butter", "Bread"], dish_type="dinner food")
    recipe_graph.add_recipe("Dahi Vada", ["Urad Dal", "Yogurt", "Tamarind", "Coriander", "Mint", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Aloo Paratha", ["Wheat Flour", "Potato", "Spices", "Butter"], dish_type="breakfast")
    recipe_graph.add_recipe("Chana Masala", ["Chickpeas", "Tomato", "Onion", "Spices", "Coriander"], dish_type="lunch food")
    recipe_graph.add_recipe("Matar Paneer", ["Paneer", "Peas", "Tomato", "Onion", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Kadhi Pakora", ["Gram Flour", "Yogurt", "Onion", "Spices", "Pakora"], dish_type="lunch food")
    recipe_graph.add_recipe("Malai Kofta", ["Potato", "Paneer", "Cream", "Cashews", "Spices", "Tomato", "Onion"], dish_type="dinner food")
    recipe_graph.add_recipe("Samosa Chaat", ["Samosa", "Chickpeas", "Yogurt", "Tamarind", "Mint", "Onion", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Chole Kulche", ["Chickpeas", "Flour", "Spices", "Yogurt", "Onion", "Coriander", "Kulcha"], dish_type="snack")
    recipe_graph.add_recipe("Rajma Chawal", ["Kidney Beans", "Rice", "Tomato", "Onion", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Kheer", ["Rice", "Milk", "Sugar", "Cardamom", "Saffron", "Almonds", "Raisins"], dish_type="sweet")
    recipe_graph.add_recipe("Shahi Paneer", ["Paneer", "Tomato", "Onion", "Cream", "Cashews", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Bhindi Masala", ["Okra", "Tomato", "Onion", "Spices", "Coriander"], dish_type="dinner food")
    recipe_graph.add_recipe("Papdi Chaat", ["Papdi", "Potato", "Chickpeas", "Yogurt", "Tamarind", "Mint", "Onion", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Mango Lassi", ["Mango", "Yogurt", "Milk", "Sugar", "Cardamom"], dish_type="beverage")
    recipe_graph.add_recipe("Idli", ["Rice", "Urad Dal"], dish_type="breakfast")
    recipe_graph.add_recipe("Dosa", ["Rice", "Urad Dal"], dish_type="breakfast")
    recipe_graph.add_recipe("Upma", ["Semolina", "Vegetables"], dish_type="breakfast")
    recipe_graph.add_recipe("Pongal", ["Rice", "Moong Dal"], dish_type="breakfast")
    recipe_graph.add_recipe("Medu Vada", ["Urad Dal", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Poha", ["Flattened Rice", "Vegetables"], dish_type="breakfast")
    recipe_graph.add_recipe("Aloo Puri", ["Potato", "Wheat Flour", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Masala Dosa", ["Rice", "Urad Dal", "Potato"], dish_type="breakfast")
    recipe_graph.add_recipe("Rava Idli", ["Semolina", "Curds", "Vegetables"], dish_type="breakfast")
    recipe_graph.add_recipe("Uttapam", ["Rice", "Urad Dal", "Vegetables"], dish_type="breakfast")
    recipe_graph.add_recipe("Butter Chicken", ["Chicken", "Tomato", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Paneer Tikka Masala", ["Paneer", "Tomato", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Dal Makhani", ["Black Lentils", "Kidney Beans", "Butter", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Chole Bhature", ["Chickpeas", "Flour", "Yogurt", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Aloo Gobi", ["Potato", "Cauliflower", "Tomato", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Biryani", ["Basmati Rice", "Chicken", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Palak Paneer", ["Paneer", "Spinach", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Rajma", ["Kidney Beans", "Tomato", "Onion", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Vegetable Pulao", ["Basmati Rice", "Assorted Vegetables", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Kadhi Pakora", ["Gram Flour", "Yogurt", "Vegetables", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Gulab Jamun", ["Khoya", "Sugar", "Flour"], dish_type="sweet")
    recipe_graph.add_recipe("Rasgulla", ["Milk", "Sugar", "Lemon Juice"], dish_type="sweet")
    recipe_graph.add_recipe("Jalebi", ["Maida", "Sugar", "Yogurt"], dish_type="sweet")
    recipe_graph.add_recipe("Kheer", ["Rice", "Milk", "Sugar", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Barfi", ["Khoya", "Sugar", "Cardamom"], dish_type="sweet")
    recipe_graph.add_recipe("Ladoo", ["Besan", "Sugar", "Ghee", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Halwa", ["Semolina", "Sugar", "Ghee", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Pedha", ["Khoya", "Sugar", "Cardamom"], dish_type="sweet")
    recipe_graph.add_recipe("Rasmalai", ["Milk", "Sugar", "Saffron", "Cardamom"], dish_type="sweet")
    recipe_graph.add_recipe("Chicken Curry", ["Chicken", "Tomato", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Fish Curry", ["Fish", "Coconut Milk", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Egg Curry", ["Egg", "Tomato", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Veg Fried Rice", ["Rice", "Assorted Vegetables", "Soy Sauce"], dish_type="lunch food")
    recipe_graph.add_recipe("Chicken Biryani", ["Basmati Rice", "Chicken", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Veg Biryani", ["Basmati Rice", "Assorted Vegetables", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Egg Fried Rice", ["Rice", "Egg", "Assorted Vegetables", "Soy Sauce"], dish_type="lunch food")
    recipe_graph.add_recipe("Chicken Tikka", ["Chicken", "Yogurt", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Veg Pulao", ["Basmati Rice", "Assorted Vegetables", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Tandoori Roti", ["Wheat Flour", "Yogurt", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Veggie Wrap", ["Assorted Vegetables", "Whole Wheat Wrap", "Hummus"], dish_type="snack")    
    recipe_graph.add_recipe("Avocado Toast", ["Avocado", "Whole Wheat Bread", "Lemon Juice", "Chili Flakes"], dish_type="breakfast")
        
    recipe_graph.add_recipe("Aloo Poha", ["Poha", "Potatoes", "Onion", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Methi Thepla", ["Whole Wheat Flour", "Fenugreek Leaves", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Ragi Idli", ["Ragi Flour", "Urad Dal"], dish_type="breakfast")
    recipe_graph.add_recipe("Besan Chilla", ["Gram Flour", "Vegetables", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Methi Paratha", ["Whole Wheat Flour", "Fenugreek Leaves", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Paneer Bhurji", ["Paneer", "Onion", "Tomato", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Sabudana Khichdi", ["Sabudana", "Potato", "Peanuts", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Rava Upma", ["Semolina", "Vegetables", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Pongal", ["Rice", "Moong Dal", "Pepper", "Cumin"], dish_type="breakfast")
    recipe_graph.add_recipe("Akki Roti", ["Rice Flour", "Vegetables", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Kande Pohe", ["Poha", "Onion", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Aloo Methi", ["Potato", "Fenugreek Leaves", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Palak Puri", ["Whole Wheat Flour", "Spinach", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Makki Ki Roti", ["Maize Flour", "Sarson Ka Saag", "Butter"], dish_type="breakfast")
    recipe_graph.add_recipe("Neer Dosa", ["Rice Flour", "Coconut", "Salt"], dish_type="breakfast")
    recipe_graph.add_recipe("Ragi Mudde", ["Ragi Flour", "Water"], dish_type="breakfast")
    recipe_graph.add_recipe("Kadambam", ["Rice", "Assorted Lentils", "Vegetables", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Kozhukattai", ["Rice Flour", "Jaggery", "Coconut"], dish_type="snack")
    recipe_graph.add_recipe("Kanda Poha", ["Poha", "Onion", "Peanuts", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Masala Oats", ["Oats", "Vegetables", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Beetroot Poriyal", ["Beetroot", "Coconut", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Avial", ["Assorted Vegetables", "Coconut", "Yogurt", "Curry Leaves"], dish_type="lunch food")
    recipe_graph.add_recipe("Semiya Upma", ["Vermicelli", "Vegetables", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Sakkarai Pongal", ["Rice", "Moong Dal", "Jaggery", "Ghee", "Dry Fruits"], dish_type="breakfast")
    recipe_graph.add_recipe("Kothimbir Vadi", ["Coriander", "Chickpea Flour", "Coconut", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Pineapple Sheera", ["Semolina", "Pineapple", "Sugar", "Ghee", "Cardamom"], dish_type="sweet")
    recipe_graph.add_recipe("Oats Uttapam", ["Oats", "Semolina", "Vegetables", "Yogurt", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Thalipeeth", ["Multigrain Flour", "Onion", "Coriander", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Aloo Kachori", ["Whole Wheat Flour", "Potato", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Dhokla Sandwich", ["Dhokla", "Green Chutney", "Tomato", "Onion"], dish_type="snack")
    recipe_graph.add_recipe("Kanda Batata Poha", ["Poha", "Onion", "Potato", "Peanuts", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Vegetable Rava Idli", ["Semolina", "Vegetables", "Yogurt", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Palak Pakora", ["Spinach", "Chickpea Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Kesari Bath", ["Semolina", "Sugar", "Ghee", "Saffron", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Aloo Bonda", ["Potato", "Chickpea Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Poori Masala", ["Whole Wheat Flour", "Potato", "Spices"], dish_type="breakfast")
    
    recipe_graph.add_recipe("Semiya Payasam", ["Vermicelli", "Milk", "Sugar", "Cardamom", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Pesarattu", ["Green Gram", "Rice", "Ginger", "Green Chilies"], dish_type="breakfast")
    recipe_graph.add_recipe("Bisi Bele Bath", ["Rice", "Toor Dal", "Vegetables", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Bhatura", ["Maida", "Yogurt", "Baking Soda", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Undhiyu", ["Assorted Vegetables", "Spices", "Coconut"], dish_type="dinner food")
    recipe_graph.add_recipe("Patra", ["Colocasia Leaves", "Chickpea Flour", "Tamarind", "Jaggery"], dish_type="snack")
    recipe_graph.add_recipe("Rava Kesari", ["Semolina", "Sugar", "Ghee", "Saffron", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Puran Poli", ["Chana Dal", "Jaggery", "Cardamom", "Wheat Flour"], dish_type="sweet")
    recipe_graph.add_recipe("Khaman Dhokla", ["Chickpea Flour", "Yogurt", "Eno Fruit Salt", "Green Chilies"], dish_type="snack")
    recipe_graph.add_recipe("Aloo Matar", ["Potato", "Peas", "Tomato", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Mutter Paneer", ["Paneer", "Peas", "Tomato", "Onion", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Vegetable Khichdi", ["Rice", "Moong Dal", "Assorted Vegetables", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Lemon Rice", ["Rice", "Lemon", "Peanuts", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Veg Momos", ["Flour", "Assorted Vegetables", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Paneer Pakora", ["Paneer", "Chickpea Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Mango Smoothie", ["Mango", "Yogurt", "Milk", "Honey"], dish_type="beverage")
    recipe_graph.add_recipe("Banana Smoothie", ["Banana", "Yogurt", "Milk", "Honey"], dish_type="beverage")
    recipe_graph.add_recipe("Chocolate Milkshake", ["Cocoa Powder", "Milk", "Sugar", "Ice Cream"], dish_type="beverage")
    recipe_graph.add_recipe("Pineapple Juice", ["Pineapple", "Water", "Sugar", "Mint"], dish_type="beverage")
    recipe_graph.add_recipe("Watermelon Juice", ["Watermelon", "Mint", "Lemon", "Sugar"], dish_type="beverage")
    recipe_graph.add_recipe("Strawberry Banana Smoothie", ["Strawberry", "Banana", "Yogurt", "Milk", "Honey"], dish_type="beverage")
    recipe_graph.add_recipe("Mango Lassi", ["Mango", "Yogurt", "Milk", "Sugar", "Cardamom"], dish_type="beverage")
    recipe_graph.add_recipe("Green Tea", ["Green Tea Leaves", "Water", "Honey", "Lemon"], dish_type="beverage")
    recipe_graph.add_recipe("Masala Chai", ["Tea Leaves", "Milk", "Water", "Spices", "Sugar"], dish_type="beverage")
    recipe_graph.add_recipe("Cold Coffee", ["Coffee", "Milk", "Sugar", "Ice Cream"], dish_type="beverage")
    recipe_graph.add_recipe("Mango Shake", ["Mango", "Milk", "Sugar"], dish_type="beverage")
    recipe_graph.add_recipe("Oreo Milkshake", ["Oreo Cookies", "Milk", "Ice Cream"], dish_type="beverage")
    recipe_graph.add_recipe("Lemonade", ["Lemon", "Water", "Sugar", "Mint"], dish_type="beverage")
    
    recipe_graph.add_recipe("Paneer Bhurji", ["Paneer", "Onion", "Tomato", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Vegetable Upma", ["Semolina", "Vegetables", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Paneer Butter Masala", ["Paneer", "Tomato", "Cream", "Butter", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Masoor Dal", ["Red Lentils", "Tomato", "Onion", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Bhindi Fry", ["Okra", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Jeera Rice", ["Basmati Rice", "Cumin Seeds", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Vegetable Sandwich", ["Assorted Vegetables", "Bread", "Cheese", "Mayonnaise"], dish_type="snack")
    recipe_graph.add_recipe("Vegetable Noodles", ["Noodles", "Assorted Vegetables", "Soy Sauce", "Spices"], dish_type="snack")
    
    recipe_graph.add_recipe("Vegetable Biryani", ["Basmati Rice", "Assorted Vegetables", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Methi Malai Paneer", ["Paneer", "Cream", "Fenugreek Leaves", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Chana Chaat", ["Chickpeas", "Onion", "Tomato", "Tamarind", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Methi Thepla", ["Whole Wheat Flour", "Fenugreek Leaves", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Aloo Bhujia", ["Potato", "Chickpea Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Vegetable Cutlet", ["Assorted Vegetables", "Potato", "Bread Crumbs", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Sabudana Khichdi", ["Sabudana", "Potato", "Peanuts", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Vegetable Manchurian", ["Assorted Vegetables", "Soy Sauce", "Corn Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Palak Paneer", ["Paneer", "Spinach", "Cream", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Mango Kulfi", ["Mango Pulp", "Milk", "Sugar", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Badam Milk", ["Almonds", "Milk", "Sugar", "Cardamom"], dish_type="beverage")
    recipe_graph.add_recipe("Chicken Korma", ["Chicken", "Yogurt", "Cream", "Spices", "Onion", "Tomato"], dish_type="dinner food")
    recipe_graph.add_recipe("Dal Tadka", ["Yellow Lentils", "Tomato", "Onion", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Egg Bhurji", ["Egg", "Onion", "Tomato", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Rajma Masala", ["Kidney Beans", "Tomato", "Onion", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Vegetable Kurma", ["Assorted Vegetables", "Coconut", "Spices", "Onion", "Tomato"], dish_type="dinner food")
    recipe_graph.add_recipe("Sprout Salad", ["Sprouts", "Vegetables", "Lemon Juice", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Quinoa Salad", ["Quinoa", "Vegetables", "Olive Oil", "Lemon Juice"], dish_type="healthy")
    recipe_graph.add_recipe("Grilled Chicken Salad", ["Chicken", "Lettuce", "Vegetables", "Olive Oil"], dish_type="healthy")
    recipe_graph.add_recipe("Oats Porridge", ["Oats", "Milk", "Honey", "Dry Fruits"], dish_type="healthy")
    recipe_graph.add_recipe("Spinach Smoothie", ["Spinach", "Banana", "Yogurt", "Honey"], dish_type="healthy")
    recipe_graph.add_recipe("Lentil Soup", ["Lentils", "Vegetables", "Tomato", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Tofu Stir Fry", ["Tofu", "Assorted Vegetables", "Soy Sauce", "Ginger", "Garlic"], dish_type="healthy")
    recipe_graph.add_recipe("Chickpea Salad", ["Chickpeas", "Vegetables", "Feta Cheese", "Olive Oil"], dish_type="healthy")
    recipe_graph.add_recipe("Ragi Porridge", ["Ragi Flour", "Milk", "Jaggery", "Dry Fruits"], dish_type="healthy")
    recipe_graph.add_recipe("Vegetable Soup", ["Assorted Vegetables", "Broth", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Tomato Soup", ["Tomato", "Vegetable Stock", "Cream", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Chicken Soup", ["Chicken", "Vegetables", "Chicken Broth", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Minestrone Soup", ["Tomato", "Beans", "Pasta", "Vegetables", "Vegetable Broth"], dish_type="healthy")
    recipe_graph.add_recipe("Mixed Vegetable Soup", ["Assorted Vegetables", "Vegetable Broth", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Corn Salad", ["Corn", "Assorted Vegetables", "Lemon Juice", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Fruit Salad", ["Assorted Fruits", "Honey", "Lemon Juice", "Mint"], dish_type="healthy")
    recipe_graph.add_recipe("Potato Salad", ["Potato", "Mayonnaise", "Mustard Sauce", "Vegetables"], dish_type="healthy")
    recipe_graph.add_recipe("Vegetable Soup", ["Assorted Vegetables", "Broth", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Tomato Soup", ["Tomato", "Vegetable Stock", "Cream", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Chicken Soup", ["Chicken", "Vegetables", "Chicken Broth", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Minestrone Soup", ["Tomato", "Beans", "Pasta", "Vegetables", "Vegetable Broth"], dish_type="healthy")
    recipe_graph.add_recipe("Mixed Vegetable Soup", ["Assorted Vegetables", "Vegetable Broth", "Spices"], dish_type="healthy")
    recipe_graph.add_recipe("Chicken Fry", ["Chicken", "Spices", "Yogurt"], dish_type="dinner food")
    recipe_graph.add_recipe("Gobi Manchurian", ["Cauliflower", "Soy Sauce", "Corn Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Egg Curry", ["Egg", "Tomato", "Onion", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Bread Upma", ["Bread", "Vegetables", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Onion Pakora", ["Onion", "Chickpea Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Bread Pakora", ["Bread", "Potato", "Chickpea Flour", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Chana Masala", ["Chickpeas", "Tomato", "Onion", "Spices"], dish_type="lunch food")
    recipe_graph.add_recipe("Paneer Pulao", ["Basmati Rice", "Paneer", "Assorted Vegetables", "Spices"], dish_type="dinner food")
    recipe_graph.add_recipe("Kaju Katli", ["Cashews", "Sugar", "Ghee", "Cardamom"], dish_type="sweet")
    recipe_graph.add_recipe("Coconut Ladoo", ["Coconut", "Condensed Milk", "Cardamom"], dish_type="sweet")
    recipe_graph.add_recipe("Malpua", ["Flour", "Sugar", "Milk", "Fennel Seeds"], dish_type="sweet")
    recipe_graph.add_recipe("Rice Kheer", ["Rice", "Milk", "Sugar", "Cardamom", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Aloo Chaat", ["Potato", "Tamarind", "Mint", "Spices"], dish_type="snack")
    recipe_graph.add_recipe("Gajar Halwa", ["Carrot", "Milk", "Sugar", "Ghee", "Dry Fruits"], dish_type="sweet")
    recipe_graph.add_recipe("Paneer Paratha", ["Whole Wheat Flour", "Paneer", "Spices"], dish_type="breakfast")
    recipe_graph.add_recipe("Fish Fry", ["Fish", "Spices", "Lemon Juice"], dish_type="dinner food")
    recipe_graph.add_recipe("Chicken 65", ["Chicken", "Spices", "Curry Leaves", "Yogurt"], dish_type="snack")
    

    # Add more recipes here as needed
    return recipe_graph 