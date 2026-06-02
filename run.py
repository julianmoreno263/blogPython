from blogr import createApp, db

app = createApp()

# Este decorador mágico creará las tablas automáticamente en Render
@app.before_request
def create_tables():
    # Remueve el decorador después de ejecutarse la primera vez para no saturar el servidor
    app.before_request_funcs[None].remove(create_tables)
    db.create_all()

if __name__ == '__main__':
    app.run()


#NOTA: PARA EJECUTAR EL PROGRAMA SE PONE EN CONSOLA: python \run.py

#El simbolo \  se saca con ALT+92.





