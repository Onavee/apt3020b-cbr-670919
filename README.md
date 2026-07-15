# ReasonRight Case-Based-System

A Python-based Case-Based Reasoning (CBR) system that recommends solutions to common small-business challenges by learning from previously solved cases.

## Student Details

-Name: Viona GItonga
-Student ID: 670919
-Course: APT3020B -Knowledge-Based Systems

- Selected Scenario: Small Business Support

## Project Description

ReasonRight CBR System is a Case-Based Reasoning (CBR) application developed to support small businesses in solving common operational challenges. The system compares a new business problem with previously solved cases stored in a case base and recommends the most suitable solution based on similarity. If the suggested solution is effective, it is reused; otherwise, the user can revise it. The solved case is then retained in the case base, allowing the system to learn from new experiences and improve its knowledge over time.

## Case-Based Reasoning Cycle

### Retrieve

The system accepts the details of a new business problem from the user and compares them with all previously stored cases in the case base. The `calculate_similarity()` function assigns weighted scores to matching attributes, while the `retrieve_best_case()` function identifies the case with the highest similarity score and presents its solution to the user.

### Reuse

Once the most similar case has been retrieved, the system recommends the solution associated with that case. This allows the user to reuse knowledge from a previously solved business problem instead of creating a solution from scratch.

### Revise

After displaying the recommended solution, the system asks the user whether the solution successfully solved the problem. If the answer is **yes**, the original solution is accepted. If the answer is **no**, the user enters a revised solution that better addresses the new business challenge.

### Retain

After the final solution has been confirmed, the system creates a new case containing the user's business details and the final solution. A new case ID is assigned, and the case is added to the case base so it can be used to solve similar problems in the future.

## Case Attributes

Each case in the case base contains the following attributes:

| Attribute               | Description                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Business Type**       | Identifies the type of business, such as a retail shop, bakery, pharmacy, or restaurant.                                     |
| **Sales Level**         | Indicates the current sales performance of the business (low, medium, or high).                                              |
| **Customer Complaints** | Shows the level of customer complaints received (none, few, or many).                                                        |
| **Stock Status**        | Describes the availability of inventory, such as available, low, or out of stock.                                            |
| **Marketing Activity**  | Indicates the level of marketing efforts being carried out by the business (none, low, medium, or high).                     |
| **Business Age**        | Shows whether the business is new or established. This attribute helps distinguish businesses at different stages of growth. |
| **Main Problem**        | Describes the primary challenge the business is facing, such as low sales, stock shortage, or customer complaints.           |
| **Solution**            | Stores the solution that successfully resolved the business problem.                                                         |

## Similarity SCoring SYstem

The RessonRight CBR System uses a weighted similarity scoring approach to compare a new business case with previously solved cases. Each matching attribute contributes a specific number of points to the overall similarity score. Attributes that have a greater impact on identifying the correct business problem are assigned higher weights.

| Attribute           | Weight | Reason                                                                                                       |
| ------------------- | -----: | ------------------------------------------------------------------------------------------------------------ |
| Main Problem        |      5 | This is the most important attribute because it identifies the primary issue the business is experiencing.   |
| Business Type       |      3 | Businesses in the same industry often experience similar challenges and require similar solutions.           |
| Sales Level         |      2 | Sales performance helps indicate the severity of the business situation.                                     |
| Customer Complaints |      2 | Customer feedback is an important indicator of service or product-related problems.                          |
| Stock Status        |      2 | Inventory availability influences many business decisions and possible solutions.                            |
| Marketing Activity  |      1 | Marketing contributes to business performance but is less significant than the main problem.                 |
| Business Age        |      1 | Whether a business is new or established provides additional context but has a smaller impact on similarity. |

The maximum possible similarity score is **16**. After comparing all previous cases, the similarity percentage is calculated using the formula:

## How to Run the Project

1. Download or clone the project files to your computer.
2. Ensure that Python 3 is installed on your system.
3. Open a terminal or command prompt and navigate to the project folder.
4. Run the program using the following command:

   ```bash
   python cbr_system.py
   ```

5. Enter the requested business details when prompted, including the business type, sales level, customer complaints, stock status, marketing activity, business age, and main business problem.
6. Review the recommended solution provided by the system.
7. Indicate whether the suggested solution worked:
   - Enter **yes** to accept the suggested solution.
   - Enter **no** to provide a revised solution.
8. The system will retain the new solved case and display the updated number of cases in the case base.

## Test Cases

```text
 ReasonRight CBR System

Describe your business (e.g.,  jewellery, wholesale, bakery, pharmacy): wholesale
Current sales level (low, medium, high): high
Customer complaints (none, few, many): many
Stock status (available, low, out of stock): available
Marketing activity (none, low, medium, high): low
Business age (new or established): established
What is the main business problem? Customer complain they don't get all their goods which they purchased

Most Similar Case
----------------------
Case ID: 2
Similarity Score: 5
Similarity Percentage: 31.25 %
Suggested Solution:
Improve customer service by training staff and responding to complaints quickly.

Did the suggested solution work? yes

Final Solution: Improve customer service by training staff and responding to complaints quickly.
New case retained successfully.
Total cases: 9
```

## Conclusion

## Conclusion

The ReasonRight CBR System demonstrates the four stages of the Case-Based Reasoning cycle by retrieving similar business cases, reusing existing solutions, allowing users to revise recommendations when necessary, and retaining newly solved cases for future use. As more cases are added to the case base, the system becomes a more valuable knowledge resource for recommending solutions to common small-business challenges.
