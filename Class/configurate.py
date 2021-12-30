import xmlrpc.client

url = 'https://demo2.odoo.com' #crear variable sobre url erp
db = 'demo_150_1638474132'  #nombre de la base de datos
username= 'admin' #usuario
password = 'admin'   # pas usuario
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url)) ## metallamado a odo
uid = common.authenticate(db, username, password, {}) ## autenticador de la meta llamada
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url)) # segunda metallamada

# models.execute_kw(db, uid, password, model, 'write', [ids, values])
# res=models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name':'nombre'}])
# res=models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name':'nombre','email':'cristianisg@gmail.com'}])
# res=models.execute_kw(db, uid, password, 'res.partner', 'read', [60])
# context = {'fields':['name','email']}
# res=models.execute_kw(db, uid, password, 'res.partner', 'read', [60],context)
# res=models.execute_kw(db, uid, password, 'res.partner', 'write', [60,{'email':'gaymostro@elcristian.com'}]) 
res=models.execute_kw(db, uid, password, 'res.partner', 'unlink', [59]) 
print(res)