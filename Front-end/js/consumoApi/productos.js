let productos_table = document.getElementById('cuerpo_productos');

window.addEventListener('load', async() => {
    const options = {method: 'GET'};
    
    const response = await fetch('http://localhost:5000' + '/getAllElements', options);
    if(response.status === 200){
        let productos = await response.json();
        let productos_final = '';
        productos.forEach(producto => {
            
           productos_final += 
           `
           <tr>
                <td class="text-center">${producto.ID_elemento}</td>
                <td class="text-center">${producto.referencia}</td>
                <td class="text-center">${producto.nombres}</td>
                <td class="text-center">${producto.cantidad}</td>
                <td class="text-center">${producto.valor}</td>    
                <td class="text-center">${producto.estado}</td>    
                <td class="text-center">${producto.lugar}</td>    
                <td class="text-center">${producto.fecha_reg}</td>    
                <td class="text-center">${producto.hora_reg}</td>    
                <td class="text-center">${producto.Observaciones}</td>    
                <td class="text-center">
                    <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                        <button type="button" class="btn btn-primary"id="modificar_producto"><a href="update_productos.html" style="color:white">Modificar</a></button>
                        <button type="button" class="btn btn-danger" id="delete" onclick="eliminar_producto(${producto.ID_elemento})">Eliminar</button>
                    </div>
              </td>
            </tr>    
           `;
           productos_table.innerHTML = productos_final;
        });
    }else{
        console.log('error');
    }
      
});