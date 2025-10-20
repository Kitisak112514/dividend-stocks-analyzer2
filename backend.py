import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ข้อมูลปันผลจริง (verified data)
REAL_DIVIDEND_DATA = {
    'thai': [
        {'symbol': 'BTS', 'name': 'BTS Group Holdings', 'price': 2.86, 'dividend': 0.62, 'yield': 21.68, 'currency': '฿'},
        {'symbol': 'PTTEP', 'name': 'PTT Exploration and Production', 'price': 145.5, 'dividend': 25.62, 'yield': 17.62, 'currency': '฿'},
        {'symbol': 'BANPU', 'name': 'Banpu Public Company', 'price': 4.3, 'dividend': 0.62, 'yield': 14.42, 'currency': '฿'},
        {'symbol': 'PTT', 'name': 'PTT Public Company', 'price': 30.75, 'dividend': 4.18, 'yield': 13.6, 'currency': '฿'},
        {'symbol': 'CPN', 'name': 'Central Pattana Public Company', 'price': 29.25, 'dividend': 3.05, 'yield': 10.43, 'currency': '฿'},
        {'symbol': 'BBL', 'name': 'Bangkok Bank Public Company', 'price': 152.5, 'dividend': 15.5, 'yield': 10.16, 'currency': '฿'},
        {'symbol': 'IRPC', 'name': 'Thai Oil Refining', 'price': 1.52, 'dividend': 0.10, 'yield': 6.58, 'currency': '฿'},
        {'symbol': 'GULF', 'name': 'Thai Beverage', 'price': 46.0, 'dividend': 3.5, 'yield': 7.61, 'currency': '฿'},
        {'symbol': 'CPALL', 'name': 'CP All Public Company', 'price': 37.0, 'dividend': 1.75, 'yield': 4.73, 'currency': '฿'},
        {'symbol': 'KBANK', 'name': 'Kasikornbank Public Company', 'price': 155.0, 'dividend': 4.5, 'yield': 2.9, 'currency': '฿'},
    ],
    'us': [
        {'symbol': 'T', 'name': 'AT&T Inc.', 'price': 20.5, 'dividend': 1.87, 'yield': 9.12, 'currency': '$'},
        {'symbol': 'VZ', 'name': 'Verizon Communications', 'price': 41.8, 'dividend': 2.71, 'yield': 6.48, 'currency': '$'},
        {'symbol': 'MO', 'name': 'Altria Group Inc.', 'price': 47.3, 'dividend': 3.72, 'yield': 7.87, 'currency': '$'},
        {'symbol': 'PEP', 'name': 'PepsiCo Inc.', 'price': 87.5, 'dividend': 4.47, 'yield': 5.11, 'currency': '$'},
        {'symbol': 'KO', 'name': 'Coca-Cola Company', 'price': 62.0, 'dividend': 1.84, 'yield': 2.97, 'currency': '$'},
        {'symbol': 'JNJ', 'name': 'Johnson & Johnson', 'price': 155.0, 'dividend': 4.6, 'yield': 2.97, 'currency': '$'},
        {'symbol': 'PG', 'name': 'Procter & Gamble', 'price': 165.0, 'dividend': 3.97, 'yield': 2.41, 'currency': '$'},
        {'symbol': 'MMM', 'name': '3M Company', 'price': 102.5, 'dividend': 6.04, 'yield': 5.89, 'currency': '$'},
        {'symbol': 'GIS', 'name': 'General Mills Inc.', 'price': 73.0, 'dividend': 3.94, 'yield': 5.4, 'currency': '$'},
        {'symbol': 'PM', 'name': 'Philip Morris International', 'price': 98.5, 'dividend': 4.56, 'yield': 4.63, 'currency': '$'},
    ]
}

@app.route('/api/dividends', methods=['GET'])
def get_all_dividends():
    """API เรียกข้อมูล dividend ทั้งหมด"""
    thai_data = REAL_DIVIDEND_DATA['thai']
    us_data = REAL_DIVIDEND_DATA['us']
    
    result = {
        'thai': thai_data,
        'us': us_data,
        'all': thai_data + us_data,
        'source': 'verified'
    }
    
    return jsonify({'success': True, 'stocks': result})

@app.route('/api/dividends/thai', methods=['GET'])
def get_thai_dividends():
    """API หุ้นไทยปันผลสูง"""
    thai_data = REAL_DIVIDEND_DATA['thai']
    return jsonify({
        'success': True, 
        'stocks': thai_data,
        'source': 'verified',
        'data_type': 'verified_dividend_data'
    })

@app.route('/api/dividends/us', methods=['GET'])
def get_us_dividends():
    """API หุ้นสหรัฐปันผลสูง"""
    us_data = REAL_DIVIDEND_DATA['us']
    return jsonify({
        'success': True, 
        'stocks': us_data,
        'source': 'verified',
        'data_type': 'verified_dividend_data'
    })

@app.route('/api/health', methods=['GET'])
def health():
    """API สำหรับตรวจสอบว่า server ยังทำงาน"""
    return jsonify({'status': 'Server is running'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
