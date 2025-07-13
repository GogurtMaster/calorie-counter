from  flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    

    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Daily_Calories ORDER By date DESC")
    entries = cursor.fetchall()

    conn.close()
    
    return render_template('index.html', entries=entries) #have to include extention

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        
        # namne inside braket must mach anmes from form
        food = request.form['food']
        protein = request.form['protein']
        calories = request.form['calories']
        date = request.form['date']

        print(f'submitted\nfood: {food}\nprotein: {protein}\ncalories: {calories}\ndate: {date}')

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Daily_Calories (food, protein, calories, date)
            VALUES (?, ?, ?, ?)
                       ''', (food, protein, calories, date))
        
        conn.commit()
        conn.close()

        return redirect('/')
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')