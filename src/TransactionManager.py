
class Transaction:
    # Class for Trnsaction handling

    def __init__(self,Transaction_Id, Amount,Date_of_Transaction, Recipient ,Sender, Purpose):
        # Set parameters for class transaction
        self.Transaction_Id = Transaction_Id
        self.Amount = Amount
        self.Date_of_Transaction = Date_of_Transaction
        self.Recipient = Recipient
        self.Sender = Sender
        self.Purpose = Purpose
    
    
    
    def New_Transaction(Amount,Date_of_Transaction, Recipient ,Sender, Purpose):
        # Method to accept values for new transaction
        pass
