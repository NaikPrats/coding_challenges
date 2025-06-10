class Generator:
    def __init__(self, invoices=None) -> None:
        self.invoices = invoices or [
            "invoiceA,2024-01-01,100",
            "invoiceB,2024-02-01,200",
            "invoiceC,2023-01-30,1000"
        ]

    def generate_note(self, payment_note: str) -> str:
        parts = payment_note.split(',')
        payment_id = parts[0].strip()
        payment_amount = parts[1].strip()
        invoice_id = parts[2].split(':')[1].strip()

        due_date = ''
        for invoice in self.invoices:
            inv_id, inv_date, _ = invoice.split(',')
            if inv_id.strip() == invoice_id:
                due_date = inv_date.strip()
                break

        return f"{payment_id} pays off {payment_amount} for {invoice_id} due on {due_date}"



if __name__ == "__main__":
    generator = Generator()
    print("Enter payment note in the format: payment_id,amount,Paying off: invoice_id")
    user_input = input("Payment Note: ").strip()

    result = generator.generate_note(user_input)
    print("\nGenerated Note:")
    print(result)
