const apiUrl = "http://127.0.0.1:8000/libros/";

async function getLibros() {
    const response = await fetch(apiUrl);
    const libros = await response.json();
    const itemsList = document.getElementById('items-list');
    const table = document.createElement('table');
    table.classList.add('table', 'table-striped', 'table-hover');

    const thead = document.createElement('thead');
    thead.innerHTML = `
        <tr>    
            <th>Id</th>
            <th>Nombre</th>
            <th>Autor</th>
            <th>Descripción</th>
            <th>Acciones</th>
        </tr>
    `;
    table.appendChild(thead);

    const tbody = document.createElement('tbody');
    libros.forEach(libro => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${libro.id}</td>
            <td>${libro.name}</td>
            <td>${libro.autor}</td>
            <td>${libro.description}</td>
            <td>
                <button class="btn btn-primary btn-sm" onclick="getLibro(${libro.id})">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="deleteLibro(${libro.id})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);

    itemsList.innerHTML = ''; 
    itemsList.appendChild(table);

}

async function submitForm(event) {
    event.preventDefault();
    const itemId = document.getElementById('item-id').value;
    const name = document.getElementById('name').value;
    const autor = document.getElementById('autor').value;
    const description = document.getElementById('description').value;

    const itemData = {
        name: name,
        autor: autor,
        description: description
    };

    let method = 'POST';
    let url = apiUrl;

    if (itemId) {
        method = 'PUT';
        url = `${apiUrl}${itemId}`;
    }

    await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(itemData)
    });

    document.getElementById('item-form').reset();
    document.getElementById('item-id').value = '';
    getLibros();
}

async function getLibro(id) {
    const response = await fetch(`${apiUrl}${id}`);
    const libros = await response.json();
    document.getElementById('item-id').value = libros.id;
    document.getElementById('name').value = libros.name; 
    document.getElementById('autor').value = libros.autor; 
    document.getElementById('description').value = libros.description; 
}

async function deleteLibro(id) { 
    await fetch(`${apiUrl}${id}`, { method: 'DELETE' }); 
    getLibros(); 
}
 
window.onload = function() { 
    getLibros();
};

document.getElementById('item-form').addEventListener('submit', function(event) {
    submitForm(event);
  });