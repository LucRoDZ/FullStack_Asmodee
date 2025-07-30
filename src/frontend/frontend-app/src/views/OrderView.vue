<template>
  <div style="margin: 2rem">
    <h2>Passer une commande</h2>

    <form @submit.prevent="submitOrder">
      <label>Nom du client :</label><br />
      <input v-model="customerName" required /><br /><br />

      <h3>Choisissez vos produits :</h3>
      <div v-for="product in products" :key="product.id">
        <label>
          <input
            type="checkbox"
            :value="product.id"
            v-model="selectedProductIds"
          />
          {{ product.name }} — {{ product.price }}€ ({{ product.category }})
        </label>
      </div>

      <br />
      <button type="submit">Commander</button>
    </form>

    <div v-if="orderSummary">
      <h3>Commande confirmée</h3>
      <p><strong>ID :</strong> {{ orderSummary.order_id }}</p>
      <p><strong>Total :</strong> {{ orderSummary.total }} €</p>
      <ul>
        <li v-for="item in orderSummary.items" :key="item.id">
          {{ item.name }} — {{ item.price }}€
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getProducts, createOrder } from '@/services/api'

const products = ref([])
const selectedProductIds = ref([])
const customerName = ref('')
const orderSummary = ref(null)

const fetchProducts = async () => {
  const res = await getProducts()
  products.value = res.data
}

const submitOrder = async () => {
  if (!customerName.value || selectedProductIds.value.length === 0) return

  const payload = {
    customer_name: customerName.value,
    product_ids: selectedProductIds.value,
  }

  try {
    const res = await createOrder(payload)
    orderSummary.value = res.data
  } catch (err) {
    console.error('Erreur commande :', err)
  }
}

onMounted(fetchProducts)
</script>
