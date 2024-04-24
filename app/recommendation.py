refined_options = {
    'American': ['American', 'Bar', 'Burgers', 'BBQ', 'Sports Bar', 'Burger', 'New American', 'Cheesecake', 'Diner', 'Grill', 'Southern'],
    'Italian': ['Italian', 'Mediterranean', 'Greek', 'Pizza', 'Pasta', 'Deli'],
    'Mexican': ['Mexican', 'Fast Food', 'Sports Bar', 'Seafood', 'Asian', 'Salvadoran', 'Grill', 'Exotic', 'Fine Dining', 'Family-friendly'],
    'Asian': ['Thai', 'Ramen', 'Seafood', 'Buffet', 'Vietnamese', 'Korean', 'Japanese', 'Chinese'],
    'Seafood': ['Seafood', 'Steak', 'Sushi'],
    'Fast Food': ['Fast Food', 'Chicken Sandwiches', 'Burgers', 'Sandwiches'],
    'Sandwiches & Deli': ['Takeout', 'Cafe', 'Bakery', 'Sandwich'],
    'Pizza': ['Pizza'],
    'Steak & BBQ': ['Steak', 'Sushi', 'Burgers'],
    'Other International': ['Eastern European', 'Pan-European', 'French', 'Jamaican', 'Dominican', 'Bangladeshi', 'Barbeque', 'African', 'Colombian', 'Wings', 'Indian', 'Exotic', 'Brunch', 'Sports Bar', 'Restaurant', 'Fine Dining'],
    'Other': ['Bar', 'Chicken', 'New American', 'Exotic', 'Brunch', 'Family-friendly', 'Sports Bar', 'Restaurant', 'French', 'Grill']
}

def get_refined_options(selected_food_type):
    return refined_options.get(selected_food_type, [])
