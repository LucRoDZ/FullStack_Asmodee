<template>
  <div style="margin-left: 2rem">
    <h2>Liste des Produits</h2>

    <label for="cat">Filtrer par catégorie:</label>
    <select id="cat" v-model="category" @change="fetchProducts">
      <option value="">Toutes</option>
      <option value="electronics">Électronique</option>
      <option value="fruits">Fruits</option>
      <option value="drink">Boissons</option>
    </select>

    <ul v-if="products.length">
      <li v-for="product in products" :key="product.id">
        <strong>{{ product.name }}</strong> — {{ product.price }}€ ({{ product.category }})
      </li>
    </ul>

    <p v-else>Aucun produit trouvé.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getProducts } from '@/services/api'

const products = ref([])
const category = ref('')

const fetchProducts = async () => {
  try {
    const res = await getProducts(category.value)
    products.value = res.data
  } catch (err) {
    console.error('Erreur lors de la récupération des produits', err)
  }
}

onMounted(fetchProducts)
</script>
