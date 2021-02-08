class Category:
    balance = 0

    def __init__(self, x):
        self.name = x.capitalize()
        self.ledger = []
        self.amount_spent = 0

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def get_balance(self):
        return self.balance

    def check_funds(self, x):
        if x > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": 0 - amount, "description": description})
            self.balance -= amount
            self.amount_spent += amount
            return True
        else:
            return False

    def transfer(self, amount, cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + cat.name)
            cat.deposit(amount, "Transfer from " + self.name)
            self.amount_spent += amount
            return True
        else:
            return False

    def __str__(self):
        num = (30 - len(self.name)) // 2
        print_list = ["*" * num, self.name, "*" * num]
        for item in self.ledger:
            amount = format(float(item["amount"]), '.2f')
            amount = str(amount)[-7:]
            description = item["description"][0:23]
            print_list.extend(("\n", description, " " * (30 - len(description) - len(amount)), amount))
        print_list.extend(("\n", "Total: ", str(self.balance)))
        return "".join(print_list)



def create_spend_chart(categories):
    num_cats = len(categories)
    spend_chart_list = ["Percentage spent by category", "\n100|", "\n 90|", "\n 80|", "\n 70|", "\n 60|", "\n 50|", "\n 40|", "\n 30|", "\n 20|", "\n 10|", "\n  0|", "\n    " + "-" * (3 * num_cats + 1)]

    total_spent = 0
    for cat in categories:
        total_spent += cat.amount_spent

    numbers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    for cat in categories:
        i = 1
        perc = cat.amount_spent * 100 / total_spent
        print(cat.name, str(perc))
        for num in numbers:
            if perc >= num:
                spend_chart_list[i] += " o "
            else:
                spend_chart_list[i] += "   "
            i += 1
    for i in range(len(numbers)):
        spend_chart_list[i + 1] += " "

    max_name_length = max([len(cat.name) for cat in categories])
    j = 0
    while j < max_name_length:
        line = ["\n    "]
        for cat in categories:
            if len(cat.name) > j:
                line.extend((" ", cat.name[j], " "))
            else:
                line.append("   ")
        line.append(" ")
        spend_chart_list.append("".join(line))
        j += 1

    spend_chart_str = "".join(spend_chart_list)
    return spend_chart_str
