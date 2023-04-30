let categorias_table = document.getElementById('cuerpo_categorias');
const Constants = {
    MAIN_URL: 'http://localhost:5000',
    LOGIN : '/login',
    REGISTRO_USUARIO: '/registro',
    CREAR_ELEMENTO: '/elements/create',
    CREAR_CATEGORIA: '/category/create',
    MODIFICAR_ELEMENTO: '/elements/update',
    MODIFICAR_CATEGORIA: '/category/update',
    ELIMINAR_ELEMENTO: '/elements/delete',
    ELIMINAR_CATEGORIA: '/category/delete',
    CONSULTAR_ELEMENTO: '/elements/read',
    CONSULTAR_CATEGORIA: '/elements/read',
    TRAER_CATEGORIAS: '/getAllCategories' 
}

window.addEventListener('load', async() => {
    const options = {method: 'GET'};
    
    const response = await fetch(Constants.MAIN_URL + Constants.TRAER_CATEGORIAS, options);
    if(response.status === 200){
        let categorias = await response.json();
        let categorias_final = '';
        categorias.forEach(categoria => {
           categorias_final += 
           `
           <tr class="categoria_container">
                <td class="text-center" id="codigo" data-id="${categoria.codigo}">${categoria.codigo}</td>
                <td class="text-center">${categoria.nombre}</td>
                <td class="text-center">${categoria.descripcion}</td>
                <td class="text-center">${categoria.observacion}</td>    
                <td class="text-center">
                    <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                        <button type="button" class="btn btn-primary" id="modificar_categoria" onclick="modificar_categoria(${categoria})">Modificar</button>
                        <button type="button" class="btn btn-danger" id="delete" onclick="eliminar_categoria(${categoria.codigo})">Eliminar</button>
                    </div>
              </td>
            </tr>    
           `;
           categorias_table.innerHTML = categorias_final;
        });
    }else{
        console.log('error');
    }
      
});