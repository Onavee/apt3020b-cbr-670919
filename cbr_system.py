# a case based reasoning system that recommends actions for common small-business challenges.

# creating case-bases
case_base = [

{
    "case_id":1,
    "business_type":"retail",
    "sales_level":"low",
    "customer_complaints":"few",
    "stock_status":"available",
    "marketing_activity":"low",
    "business_age":"new",
    "main_problem":"low sales",
    "solution":"Increase online marketing through Instagram and WhatsApp promotions."
},

{
    "case_id":2,
    "business_type":"restaurant",
    "sales_level":"medium",
    "customer_complaints":"many",
    "stock_status":"available",
    "marketing_activity":"medium",
    "business_age":"established",
    "main_problem":"customer complaints",
    "solution":"Improve customer service by training staff and responding to complaints quickly."
},

{
    "case_id":3,
    "business_type":"grocery",
    "sales_level":"high",
    "customer_complaints":"few",
    "stock_status":"low",
    "marketing_activity":"low",
    "business_age":"established",
    "main_problem":"stock shortage",
    "solution":"Restock fast-moving products before inventory runs out."
},

{
    "case_id":4,
    "business_type":"jewelry",
    "sales_level":"low",
    "customer_complaints":"few",
    "stock_status":"available",
    "marketing_activity":"none",
    "business_age":"new",
    "main_problem":"low sales",
    "solution":"Launch social media campaigns, adverstisment  and partner with local influencers."
},

{
    "case_id":5,
    "business_type":"electronics",
    "sales_level":"medium",
    "customer_complaints":"few",
    "stock_status":"available",
    "marketing_activity":"high",
    "business_age":"established",
    "main_problem":"high expenses",
    "solution":"Reduce unnecessary operational costs and review supplier prices."
},

{
    "case_id":6,
    "business_type":"pharmacy",
    "sales_level":"medium",
    "customer_complaints":"few",
    "stock_status":"low",
    "marketing_activity":"low",
    "business_age":"established",
    "main_problem":"stock shortage",
    "solution":"Increase reorder frequency for essential medicines."
},

{
    "case_id":7,
    "business_type":"bakery",
    "sales_level":"low",
    "customer_complaints":"many",
    "stock_status":"available",
    "marketing_activity":"medium",
    "business_age":"new",
    "main_problem":"customer complaints",
    "solution":"Improve product quality and gather customer feedback regularly."
},

{
    "case_id":8,
    "business_type":"bookshop",
    "sales_level":"medium",
    "customer_complaints":"few",
    "stock_status":"available",
    "marketing_activity":"none",
    "business_age":"established",
    "main_problem":"low sales",
    "solution":"Introduce loyalty programs and advertise on local social media pages."
}

]

# Getting a new case
def get_new_case():
    new_case = {
        "business_type": input(
            "Describe your business (e.g.,  jewellery, wholesale, bakery, pharmacy): "
        ).lower(),
        "sales_level": input(
            "Current sales level (low, medium, high): "
        ).lower(),
        "customer_complaints": input(
            "Customer complaints (none, few, many): "
        ).lower(),
        "stock_status": input(
            "Stock status (available, low, out of stock): "
        ).lower(),
        "marketing_activity": input(
            "Marketing activity (none, low, medium, high): "
        ).lower(),
        "business_age": input(
            "Business age (new or established): "
        ).lower(),
        "main_problem": input(
            "What is the main business problem? "
        ).lower()
    }

    return new_case

# Similarity function
def calculate_similarity(new_case, previous_case):

    score = 0

    if new_case["main_problem"] == previous_case["main_problem"]:
        score += 5

    if new_case["business_type"] == previous_case["business_type"]:
        score += 3

    if new_case["sales_level"] == previous_case["sales_level"]:
        score += 2

    if new_case["customer_complaints"] == previous_case["customer_complaints"]:
        score += 2

    if new_case["stock_status"] == previous_case["stock_status"]:
        score += 2

    if new_case["marketing_activity"] == previous_case["marketing_activity"]:
        score += 1

    if new_case["business_age"] == previous_case["business_age"]:
        score += 1

    return score

# REtriving the best Case
def retrieve_best_case(new_case):

    best_case = None
    best_score = -1

    for case in case_base:

        score = calculate_similarity(new_case, case)

        if score > best_score:
            best_score = score
            best_case = case

    return best_case, best_score



# TEsting the program
print(" ReasonRight CBR System")

new_case = get_new_case()

best_case,best_score = retrieve_best_case(new_case)

maximum_score = 16

percentage = (best_score/maximum_score)*100

print("\nMost Similar Case")
print("----------------------")
print("Case ID:",best_case["case_id"])
print("Similarity Score:",best_score)
print("Similarity Percentage:",round(percentage,2),"%")
print("Suggested Solution:")
print(best_case["solution"])

answer = input("\nDid the suggested solution work? ").lower()

if answer=="yes":
    final_solution=best_case["solution"]

else:
    final_solution=input("Enter revised solution: ")

new_case["case_id"]=len(case_base)+1
new_case["solution"]=final_solution

case_base.append(new_case)

print("\nFinal Solution:",final_solution)
print("New case retained successfully.")
print("Total cases:",len(case_base))


    