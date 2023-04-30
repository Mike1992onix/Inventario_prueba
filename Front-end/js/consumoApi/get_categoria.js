let MAIN_URL = 'http://localhost:5000';
let CONSULTAR_CATEGORIA = '/elements/read';

document.addEventListener('DOMContentLoaded', () => {
  let modificar = document.querySelector('#modificar_categoria');

  if (modificar) {
    modificar.addEventListener('click', () => {
      // código para modificar categoría
    });
  }
});

    /* const options = {
    method: 'GET',
    };
    let codigo = 666; 
    const response = await fetch(`http://localhost:5000/category/read/${codigo}`, options);
    if(response.status === 200){
        let data = await response.json();
        console.log(data);
    } */
      
