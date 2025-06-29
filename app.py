from flask import Flask, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

jobs = [
{
        "id": 1,
        "title": "Customer Service Representative",
        "company": "SupportLink",
        "location": "Remote (India)",
        "description": "Provide customer service support via phone, email, or chat. No previous experience required, training provided."
    },
    {
        "id": 2,
        "title": "Warehouse Associate",
        "company": "SwiftLogistics",
        "location": "Mumbai, Maharashtra",
        "description": "Assist with inventory management and packing orders. Physical requirements include light lifting and standing for extended periods."
    },
    {
        "id": 3,
        "title": "Remote Data Entry Clerk",
        "company": "DataWorks",
        "location": "Remote (India)",
        "description": "Enter and organize data for clients, working from home. Requires basic computer skills, with no previous office experience necessary."
    },
    {
        "id": 4,
        "title": "Handyman / Maintenance Worker",
        "company": "HomeFixer",
        "location": "Bangalore, Karnataka",
        "description": "Assist with small home repairs and maintenance tasks. Flexible hours and training provided."
    },
    {
        "id": 5,
        "title": "Retail Sales Associate",
        "company": "AffordableGoods",
        "location": "Delhi, NCR",
        "description": "Assist customers in finding products, manage cash register, and maintain store cleanliness. On-the-job training is provided."
    },
    {
        "id": 6,
        "title": "Food Delivery Driver",
        "company": "QuickMeals",
        "location": "Chennai, Tamil Nadu",
        "description": "Deliver food orders to customers. Requires a reliable vehicle and valid driver's license. Flexible schedule available."
    },
    {
        "id": 7,
        "title": "Assembly Line Worker",
        "company": "EasyBuild",
        "location": "Hyderabad, Telangana",
        "description": "Work on the production line assembling products. No experience needed, paid training offered."
    },
    {
        "id": 8,
        "title": "Call Center Representative",
        "company": "AnswerPro",
        "location": "Pune, Maharashtra",
        "description": "Provide customer support for various clients via phone. Comfortable working environment with flexible hours."
    },
    {
        "id": 9,
        "title": "Pet Care Assistant",
        "company": "PawsitiveCare",
        "location": "Goa",
        "description": "Provide basic pet care services such as feeding, walking, and grooming. Suitable for animal lovers, no formal experience needed."
    },
    {
        "id": 10,
        "title": "Community Outreach Assistant",
        "company": "HopeWorks",
        "location": "Kolkata, West Bengal",
        "description": "Assist with local community outreach programs and events, focusing on helping underserved populations. No prior experience required."
    },
    {
        "id": 11,
        "title": "Cleaning Staff",
        "company": "SparkleClean",
        "location": "Ahmedabad, Gujarat",
        "description": "Maintain cleanliness in office or residential spaces. Physical work with flexible hours and minimal prior experience needed."
    },
    {
        "id": 12,
        "title": "Transportation Assistant",
        "company": "EasyTransport",
        "location": "Jaipur, Rajasthan",
        "description": "Assist with transporting individuals to and from appointments. Requires a valid driver's license, no formal education required."
    },
    {
        "id": 13,
        "title": "Gardening Assistant",
        "company": "GreenThumb",
        "location": "Chandigarh",
        "description": "Help with maintaining gardens and landscapes. Ideal for those with an interest in plants and outdoor work. Training available."
    },
    {
        "id": 14,
        "title": "Barista / Café Assistant",
        "company": "LocalBrew",
        "location": "Bangalore, Karnataka",
        "description": "Prepare and serve coffee and food in a café setting. Customer service experience is helpful, but not required. On-the-job training provided."
    },
    {
        "id": 15,
        "title": "Digital Content Moderator",
        "company": "WebSafe",
        "location": "Remote (India)",
        "description": "Review and moderate online content to ensure safety and compliance with community guidelines. Requires attention to detail and basic internet navigation skills."
    }
]
@app.route('/api/v1/job/getjobs', methods=['GET'])
def get_jobs():
    return jsonify(jobs)

@app.route("/")
def home():
    return render_template("login.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501)
