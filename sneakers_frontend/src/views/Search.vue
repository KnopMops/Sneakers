<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Поиск</h1>
                <h2 class="is-size-5 has-text-grey">Поисковый запрос: "{{ query }}"</h2>
            </div>
        </div>

        <ProductBox v-for="product in products" v-bind:key="product.id" v-bind:product="product" />
    </div>
</template>

<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast';
    import ProductBox from '@/components/ProductBox.vue';

    export default {
        name: 'Search',
        components: {
            ProductBox
        },
        data() {
            return {
                products: [],
                query: ''
            }
        },
        mounted() {
            let uri = window.location.search.substring(1)
            let params = new URLSearchParams(uri)

            if (params.get('query')) {
                this.query = params.get('query')

                this.performSearch()
            }
            document.title = `Поиск по запросу (${this.query}) | Sneakers`
        },
        methods: {
            async performSearch() {
                this.$store.commit('setIsLoading', true)

                await axios
                    .post('/api/v1/products/search/', {'query': this.query})
                    .then(response => {
                        this.products = response.data
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