
class YELPCategories:
    
    categoriesdata = {
        "active": "Active Life",
        "food": "Food",
        "health": "Health & Medical",
        "shopping": "Shopping",
        "localservices": "Local Services"
    }

    subcategoriesdata = {
        "active": {
            "amusementparks": "Amusement Parks",
            "aquariums": "Aquariums",
            "beaches": "Beaches",
            "bungeejumping": "Bungee Jumping",
            "fitness": "Fitness & Instruction",
            "gokarts": "Go Karts",
            "parks": "Parks",
            "swimmingpools": "Swimming Pools",
            "waterparks": "Water Parks"
        },
        "food": {
            "coffee": "Coffee & Tea",
            "grocery": "Grocery",
            "icecream": "Ice Cream & Frozen Yogurt",
            "foodtrucks": "Food Trucks",
            "gourmet": "Specialty Food",
            "restaurants": "Restaurants"
        },
        "health": {
            "chiropractors": "Chiropractors",
            "dentists": "Dentists",
            "diagnosticservices": "Diagnostic Services",
            "emergencyrooms": "Emergency Rooms",
            "hospitals": "Hospitals",
            "physicians": "Doctors",
            "urgent_care": "Urgent Care"
        },
        "localservices": {
            "3dprinting": "3D Printing",
            "bicycles": "Bicycles",
            "busrental": "Bus Rental",
            "electronicsrepair": "Electronics Repair",
            "homeappliancerepair": "Appliances & Repair",
            "laundryservices": "Laundry Services"
        },
        "shopping": {
            "artsandcrafts": "Arts & Crafts",
            "drugstores": "Drugstores",
            "fashion": "Fashion",
            "flowers": "Flowers & Gifts",
            "media": "Books, Mags, Music & Video",
            "publicmarkets": "Public Markets",
            "sportgoods": "Sporting Goods",
            "wholesale_stores": "Wholesale Stores"
        }
    }

    def __init__(self):
        pass
        
    def getcategories(self):
        return self.categoriesdata
    
    def getsubcategories(self, category):
        return self.subcategoriesdata[category]