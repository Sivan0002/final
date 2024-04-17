from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        Num_Bank_Accounts = float(request.form['Num_Bank_Accounts'])
        Num_Credit_Card = float(request.form['Num_Credit_Card'])
        Interest_Rate = float(request.form['Interest_Rate'])
        Num_of_Loan = float(request.form['Num_of_Loan'])
        Delay_from_due_date = float(request.form['Delay_from_due_date'])
        Outstanding_Debt = float(request.form['Outstanding_Debt'])
        Monthly_Inhand_Salary = float(request.form['Monthly_Inhand_Salary'])
        Credit_History_Age = float(request.form['Credit_History_Age'])
        Total_EMI_per_month = float(request.form['Total_EMI_per_month'])
        Monthly_Balance = float(request.form['Monthly_Balance'])
        
        
        features = [[Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Num_of_Loan, Delay_from_due_date, Outstanding_Debt, Monthly_Inhand_Salary, Credit_History_Age, Total_EMI_per_month, Monthly_Balance]]
        
        model = pickle.load(open('model.pkl', 'rb'))
        
        prediction = model.predict(features)
        


        defaulter_mapping = {0: 'Good', 1: 'Poor', 2: 'Standard'}
        predicted_result = defaulter_mapping[prediction[0]]
        

    return render_template('prediction.html', result=predicted_result)



if __name__ == '__main__':
    app.run(port=5001)