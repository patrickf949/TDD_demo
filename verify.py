all=[1,2,3,4,5,6,7,8,9]
pending =[6,7,8,9]
delivered = [1,2,3,4,5]
def check_order_status(order_id):
    if order_id in delivered:
        return True
    else:
        return False

def check_order_status_pending(order_id):
    if order_id in pending:
        return True
    else:
        return False

def add_new_order(order_id):
    if check_if_id_exists(order_id) is True:
        return False
    else:
        all.append(order_id)
        pending.append(order_id)
        return True

def check_if_id_exists(order_id):
    if order_id in all:
        return True
    else:
        return False

def add_to_delivered(order_id):
    if check_order_status(order_id) is True:
        return 'Already Delivered'
    if check_if_id_exists(order_id) is True:
        delivered.append(order_id)
        pending.remove(order_id)
        return True
    else:
        return 'Non existent'
    