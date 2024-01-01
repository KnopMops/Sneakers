<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Авторизация</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Имя пользователя</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username" />
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password" />
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Войти</button>
                        </div>
                    </div>

                    <hr>

                    Нету аккаунта? <router-link to="/signup">Зарегистрироваться</router-link>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast';

    export default {
        name: 'LogIn',
        data() {
            return {
                username: '',
                password: '',
                password2: '',
                errors: []
            }
        },
        mounted() {
            document.title = 'Авторизация | Sneakers'
        },
        methods: {
            async submitForm() {
                axios.defaults.headers.common['Authorization'] = ""
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                        .post("/api/v1/token/login/", formData)
                        .then(response => {
                            const token = response.data.auth_token
                            this.$store.commit('setToken', token)
                            axios.defaults.headers.common['Authorization'] = "Token " + token
                            localStorage.setItem("token", token)

                            toast({
                                message: 'Вы успешно вошли',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'top-right'
                            })

                            const toPath = this.$route.query.to || '/my_account'
                            this.$router.push(toPath)
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }

                                toast({
                                    message: `${error}`,
                                    type: 'is-danger',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    duration: 2000,
                                    position: 'top-right'
                                })
                            } else if (error.message) {
                                this.errors.push('Произошла ошибка. Попробуйте позже')
                                toast({
                                    message: 'Произошла ошибка. Попробуйте позже',
                                    type: 'is-danger',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    duration: 2000,
                                    position: 'top-right'
                                })
                            }
                        })
            }
        }
    }
</script>