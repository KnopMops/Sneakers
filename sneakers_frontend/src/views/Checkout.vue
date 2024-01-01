<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Оплата</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thread>
                        <tr>
                            <th>Продукт</th>
                            <th>Цена</th>
                            <th>Кол-во</th>
                            <th>Итоговая цена</th>
                            <th></th>
                        </tr>
                    </thread>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                            <td>{{ item.product.name }}</td>
                            <td>{{ item.product.price }} ₽</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ getItemTotal(item).toFixed(2) }} ₽</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Итоговая цена</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>{{ cartTotalPrice.toFixed(2) }} ₽</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Детали доставки</h2>
                <p class="has-text-grey mb-4">* Все поля обязательны</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>Имя*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name" />
                            </div>
                        </div>

                        <div class="field">
                            <label>Фамилия*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name" />
                            </div>
                        </div>

                        <div class="field">
                            <label>Почта*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email" />
                            </div>
                        </div>

                        <div class="field">
                            <label>Телефон*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone" />
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Адрес*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address" />
                            </div>
                        </div>

                        <div class="field">
                            <label>ZIP-код*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode" />
                            </div>
                        </div>

                        <div class="field">
                            <label>Место проживания*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place" />
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-dark" @click="submitForm">Оплатить</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast';

    export default {
        name: 'Checkout',
        mounted() {
            document.title = 'Оплата | Sneakers'
            this.cart = this.$store.state.cart

            if (this.cartTotalLength > 0) {
                this.stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx')
                const elements = this.stripe.elements()
                this.card = elements.create('card', { hidePostalCode: true })

                this.card.mount('#card-element')
            }
        },
        data() {
            return {
                cart: {
                    items: [],
                },
                stripe: {},
                card: {},
                first_name: '',
                last_name: '',
                email: '',
                phone: '',
                address: '',
                zipcode: '',
                place: '',
                errors: []
            }
        },
        methods: {
            getItemTotal(item) {
                return item.quantity * item.product.price
            },
            submitForm() {
                if (this.first_name === '') {
                    this.errors.push('Имя обязательное поле')
                    toast({
                        message: 'Имя обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                }

                if (this.last_name === '') {
                    this.errors.push('Фамилия обязательное поле')
                    toast({
                        message: 'Фамилия обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                }

                if (this.email === '') {
                    this.errors.push('Почта обязательное поле')
                    toast({
                        message: 'Почта обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                }

                if (this.phone === '') {
                    this.errors.push('Телефон обязательное поле')
                    toast({
                        message: 'Телефон обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                }

                if (this.address === '') {
                    this.errors.push('Адрес обязательное поле')
                    toast({
                        message: 'Адрес обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                }

                if (this.zipcode === '') {
                    this.errors.push('ZIP-код обязательное поле')
                    toast({
                        message: 'ZIP-код обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                }

                if (this.place === '') {
                    this.errors.push('Место проживания обязательное поле')
                    toast({
                        message: 'Место проживания обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                }

                if (!this.errors.length) {
                    this.$store.commit('setIsLoading', true)
                    this.stripe.createToken(this.card).then(result => {
                        if (result.error) {
                            this.$store.commit('setIsLoading', false)
                            toast({
                                    message: 'Произошла ошибка. Попробуйте позже',
                                    type: 'is-danger',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    duration: 2000,
                                    position: 'top-right'
                            })
                            this.errors.push('Произошла ошибка. Попробуйте позже')
                        } else {
                            this.stripeTokenHandler(result.token)
                        }
                    })
                }
            },
            async stripeTokenHandler(token) {
                const items = []
                for (let i = 0; i < this.cart.items.length; i++) {
                    const item = this.cart.items[i]
                    const obj = {
                        product: item.product.id,
                        quantity: item.quantity,
                        price: item.product.price * item.quantity
                    }

                    items.push(obj)
                }

                const data = {
                    'first_name': this.first_name,
                    'last_name': this.last_name,
                    'email': this.email,
                    'address': this.address,
                    'zipcode': this.zipcode,
                    'place': this.place,
                    'phone': this.phone,
                    'items': items,
                    'stripe_token': token.id,
                }

                await axios
                    .post('/api/v1/checkout/', data)
                    .then(response => {
                        this.$store.commit('clearCart')
                        this.$router.push('/cart/success')
                    })
                    .catch(error => {
                        toast({
                                    message: 'Произошла ошибка. Попробуйте позже',
                                    type: 'is-danger',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    duration: 2000,
                                    position: 'top-right'
                        })
                        this.errors.push('Произошла ошибка. Попробуйте позже')
                    })
            }
        },
        computed: {
            cartTotalPrice() {
                return this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.product.price * curVal.quantity 
                }, 0)
            },
            cartTotalLength() {
                return this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.quantity 
                }, 0)
            }
        }
    }
</script>