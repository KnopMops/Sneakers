<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Мой аккаунт</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Выйти</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">Мои заказы</h2>
                <OrderSummary v-for="order in orders" v-bind:key="order.id" v-bind:order="order" />
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast'; 
    import OrderSummary from '@/components/OrderSummary.vue'

    export default {
        name: 'MyAccount',
        mounted() {
            document.title = 'Мой аккаунт | Sneakers'
            this.getMyOrders()
        },
        components: {
            OrderSummary
        },
        data() {
                return {
                    orders: []
                }
            },
        methods: {
            logout() {
                axios.defaults.headers.common['Authorization'] = ""

                localStorage.removeItem('token')
                localStorage.removeItem('username')
                localStorage.removeItem('userid')

                this.$store.commit('removeToken')
                this.$router.push('/')
            },
            async getMyOrders() {
                this.$store.commit('setIsLoading', true)
                
                await axios
                    .get('/api/v1/orders/')
                    .then(response => {
                        this.orders = response.data
                    })
                    .catch(error => {
                        toast({
                            message: `${error}`,
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