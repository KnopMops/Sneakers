<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p style="color: red;" class="title mb-6">С Новым Годом!</p>
        <p class="subtitle">
          Добро пожаловать в
        </p>
        <p class="subtitle">
          Sneakers
        </p>
      </div>
    </section>
    
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Последнии продукты</h2>
      </div>

      <ProductBox v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product" />
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import { toast } from 'bulma-toast';
  import ProductBox from '@/components/ProductBox.vue';
  
  export default {
    name: 'HomeView',
    data() {
      return {
        latestProducts: []
      }
    },
    components: {
      ProductBox
    },
    mounted() {
      this.getLatestProducts()

      document.title = 'С Новым Годом'
    },
    methods: {
      async getLatestProducts() {
        this.$store.commit('setIsLoading', true)

        await axios
          .get('/api/v1/latest-products/')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
            toast({
                    message: 'Произошла ошибка. Попробуйте позже',
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'top-right'
            })
          })

        this.$store.commit('setIsLoading', false)
      }
    }
  }
</script>