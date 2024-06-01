from flask import Flask, request, jsonify
from clickhouse_driver import Client
from catboost import CatBoostClassifier
import pandas as pd
import os

app = Flask(__name__)

# Настройки ClickHouse
clickhouse_host = os.environ['CLICKHOUSE_HOST']
clickhouse_port = os.environ['CLICKHOUSE_PORT']
clickhouse_user = os.environ['CLICKHOUSE_USER']
clickhouse_password = os.environ['CLICKHOUSE_PASSWORD']
clickhouse_db = os.environ['CLICKHOUSE_DB']

client = Client(host=clickhouse_host, port=clickhouse_port, user=clickhouse_user, password=clickhouse_password, database=clickhouse_db)

@app.route('/')
def index():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        df = pd.read_csv(file)
        # Предположим, что у нас есть обученная модель CatBoost
        # model = CatBoostClassifier()
        # model.load_model('model.cbm')
        # predictions = model.predict(df)
        
        # Пример вставки данных в ClickHouse
        data = df.to_dict('records')
        client.execute("CREATE TABLE IF NOT EXISTS dataset (columns...) ENGINE = MergeTree() ORDER BY column_name")
        client.execute("INSERT INTO dataset VALUES", data)
        
        return 'ok'
        return jsonify(predictions.tolist())
    return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)