test_data = {12341234:{"pin": 301938, "account":{1:40}},
             12345678:{"pin": 692837, "account":{1:100, 2:35830}},
             98765432:{"pin": 394823, "account":{1:4938}},
             37482937:{"pin": 847892, "account":{1:49946, 2:100, 3:45900}}
            }

class ATM_Controller(object):
    def __init__(self):
        self.data = test_data
        self.card_inserted = False
        
    def insert_card(self, cardnumber):
        if cardnumber in self.data: 
            self.card_inserted = True
    
    def return_info(self, cardnumber):
        return self.data[cardnumber]["pin"], self.data[cardnumber]["account"]
    
    def check_pin_number(self, cardnumber):
        try_pin_number = 3
        while atm.card_inserted:
            pin, accounts = self.return_info(cardnumber)
            try_pin_number -= 1
            pin_input = input("ENTER YOUR PIN NUMBER: ")
            if pin_input.isdigit() and pin == int(pin_input):
                self.select_account(accounts) 
                print("THANK YOU FOR BANKING WITH US")
                break
            print("!!!!!WRONG PIN NUMBER!!!!!")
            if try_pin_number == 0:
                atm.card_inserted = False
                print("YOU ENTERED INCORRECT PIN NUMBER 3 TIMES.\nPLEASE TRY AGAIN.\n")
    
    def select_account(self, accounts):
        print("ACCOUNT LIST:", list(accounts.keys()))
        selected = int(input("PLEASE SELECT AN ACCOUNT: "))
        while selected not in accounts:
            print("!!!!!TRY AGAIN!!!!!")
            selected = int(input("PLEASE SELECT AN ACCOUNT: "))
        self.select_transaction(accounts, selected)
    
    def select_transaction(self, accounts, selected_acc):
        transaction = int(input("PLEASE SELECT A TRANSACTION:\n1.Balance Inquiry \n2.Deposit \n3.Cash Withdrawal \n"))
        # Balance Inquiry
        if transaction == 1:
            print("ACCOUNT BALANCE: $"+str(accounts[selected_acc])+"\n")
            self.ask_another_transaction(accounts, selected_acc)
        # Deposit
        elif transaction == 2:
            deposit = int(input("PLEASE INSERT YOUR CASH: $"))
            accounts[selected_acc] += deposit
            print("NOW YOUR ACCOUNT BALANCE IS $"+str(accounts[selected_acc])+"\n")
            self.ask_another_transaction(accounts, selected_acc)
        # Cash Withdrawal
        elif transaction == 3:
            withdrawal = int(input("ENTER THE AMOUNT YOU WISH TO WITHDRAW: $"))
            while withdrawal > accounts[selected_acc]:
                print("!!!!!FAILED!!!!!")
                withdrawal = int(input("ENTER THE AMOUNT YOU WISH TO WITHDRAW: $"))
            accounts[selected_acc] -= withdrawal
            print("TRANSACTION SUCCESSFUL")
            print("NOW YOUR ACCOUNT BALANCE IS $"+str(accounts[selected_acc])+"\n")
            self.ask_another_transaction(accounts, selected_acc)
        else:
            print("!!!!!TRY AGAIN!!!!!")
            self.select_transaction(accounts, selected_acc)
    
    def ask_another_transaction(self, accounts, selected_acc):
        another_trans = int(input("WOULD YOU LIKE TO MAKE ANOTHER TRANSACTION? \n1.YES \n2.NO \n"))
        if another_trans == 1:
            self.select_transaction(accounts, selected_acc)
        elif another_trans == 2:
            self.card_inserted = False
        else:
            print("!!!!!TRY AGAIN!!!!!")
            self.ask_another_transaction(accounts, selected_acc)
        
        
if __name__ == '__main__':
    atm = ATM_Controller()
    try:
        card = int(input("PLEASE INSERT YOUR CARD:"))
        atm.insert_card(card)
        if atm.card_inserted:
            atm.check_pin_number(card)
        else:
            print("PLEASE INSERT YOUR CARD AGAIN")
    except:
        atm.card_inserted = False
        print("SOMETHING WENT WRONG. PLEASE TRY AGAIN")
        
    

