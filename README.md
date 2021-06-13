# ATM_Controller
It is a code for a simple ATM.

**`class ATM_Controller(object)`** <br>
> Insert Card ➡️ Enter PIN Number ➡️ Select an Account ➡️ Check Balance/Deposit/Withdraw
- `__init__(self)`
  - This is a constructor for the class ATM_Controller
  - `self.data` takes test_data and `self.card_inserted` default status is "False"
- `insert_card(self,cardnumber)`
  - When a customer inserts a valid card, it changes `self.card_inserted`'s status to "True" 
- `return_info()`
  - It returns a customer's PIN number and account information using cardnumber from `self.data`.
- `check_pin_number()`
  - When a customer enters PIN number, it checks if the number is correct.
  - If a customer enters wrong number 3 times, it terminates the system. 
  - Else a customer can continue the next step.
- `select_account()`
  - It shows a customer's account list and let the customer select one of them. 
- `select_transaction`
  - A customer can select a transaction among these options: "Balance Inquiry", "Deposit", and "Cash Withdrawl"
- `ask_another_transaction()`
  - It asks if a customer needs another transaction.
  - If "YES", customer can continue another transaction; If "NO", the system is terminated. 

## Running the Project
Clone this project and execute the file by running in the command line
``` 
git clone https://github.com/kimsoojee/ATM_Controller.git
```
```
python3 atm_controller.py
```
