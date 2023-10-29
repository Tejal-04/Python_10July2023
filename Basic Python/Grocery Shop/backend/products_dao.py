from sql_connection import get_sql_connection

def get_all_products(connection):
    # Database Connection
    '''cnx = mysql.connector.connect(user='root',password='Tejal@2023',
                                host='127.0.0.1',
                                database='grocery_store')'''
    # Database Querying
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products INNER JOIN uom ON products.uom_id = uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'name':name,
                'uom_id':uom_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ('INSERT INTO products(name, uom_id, price_per_unit)VALUES(%s,%s,%s)')
    data = (product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid

'''def edit_product(connection,product_id):
    cursor = connection.cursor()
    query = ('UPDATE products SET name=product_name,uom_id=uom_id,price_per_unit=price_per_unit WHERE product_id=product_id')
    data = (product_id['product_name'],product_id['uom_id'],product_id['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()'''

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ('DELETE FROM products where product_id=' + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    
    '''print(insert_new_product(connection,{
        'product_name':'karela',
        'uom_id':'1',
        'price_per_unit':'20'
    }))'''
    
    '''print(edit_product(connection,18))'''
    
    print(delete_product(connection,19))