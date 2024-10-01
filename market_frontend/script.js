async function fetchProducts() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/product/');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            console.log(data);
            displayProducts(data.results);
        } catch (error) {
            console.error('There has been a problem with your fetch operation:', error);
        }
    }

    function displayProducts(products) {
        const productList = document.getElementById('product-list');
        productList.innerHTML = '';

        if (Array.isArray(products)) {
            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.className = 'product';
                productDiv.innerHTML = `
                    <img src="${product.photo}" alt="${product.name}">
                    <div class="product-info">
                        <h2>${product.name}</h2>
                        <p>Prix: $${product.price}</p>
                        <p>${product.description}</p>
                    </div>
                `;
                productList.appendChild(productDiv);
            });
        } else {
            console.error('Expected products to be an array, but got:', products);
        }
    }

    window.onload = fetchProducts;