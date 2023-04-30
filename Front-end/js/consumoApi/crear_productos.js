// se instancia una variable con el id del boton del html 
let btn_crear_elementos = document.getElementById('enviar-productos');
let formulario = document.getElementById('formulario_productos');

btn_crear_elementos.addEventListener('click', async(event) => {
    //evita que la pagina se recarge
    event.preventDefault();
    // traer la data del formulario 
    var datos = new FormData(formulario);

    //simula el json que envia en el postman, si no se requiere no se envia o se puede enviar los datos por la url en metodos DELETE Y GET
    const options = {
        method: 'POST',
        body: JSON.stringify({
            referencia : datos.get('referencia'),
            nombres : datos.get('nombres'),
            cantidad: datos.get('cantidad'),
            valor : datos.get('valor'),
            estado : datos.get('estado'),
            lugar: datos.get('lugar'),
            Observaciones: datos.get('lugar'),
            id_categoria: datos.get('categoria'),
        }),
        headers: {
            'Content-Type': 'application/json'
        }
      };
    
      const response = await fetch('http://localhost:5000/elements/create', options);

      if(response.status === 201){
        console.log('producto creado exitosamente');
      }else{
        console.log('error');
      }

});