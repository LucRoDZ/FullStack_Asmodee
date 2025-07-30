<template>
  <div style="margin: 2rem">
    <h2>Historique des commandes</h2>

    <div v-if="orders.length === 0">
      Aucune commande passée pour le moment.
    </div>

    <div v-else>
      <div v-for="order in orders" :key="order.order_id" style="margin-bottom: 1.5rem">
        <h4>Commande #{{ order.order_id }}</h4>
        <p><strong>Client :</strong> {{ order.customer_name }}</p>
        <p><strong>Total :</strong> {{ order.total }} €</p>
        <ul>
          <li v-for="item in order.items" :key="item.id">
            {{ item.name }} — {{ item.price }}€ ({{ item.category }})
          </li>
        </ul>
        <hr />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getOrders } from '@/services/api'

const orders = ref([])

const fetchOrders = async () => {
  try {
    const res = await getOrders()
    orders.value = res.data
  } catch (err) {
    console.error('Erreur lors du chargement des commandes', err)
  }
}

onMounted(fetchOrders)
</script>
