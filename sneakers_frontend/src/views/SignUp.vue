<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Регистрация</h1>
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

                    <div class="field">
                        <label>Повторите пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2" />
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Зарегистрироваться</button>
                        </div>
                    </div>

                    <hr>

                    Уже есть аккаунт? <router-link to="/log-in">Войти</router-link>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast';

    export default {
        name: 'SignUp',
        data() {
            return {
                username: '',
                password: '',
                password2: '',
                errors: []
            }
        },
        mounted() {
            document.title = 'Регистрация | Sneakers'
        },
        methods: {
            submitForm() {
                this.errors = []

                if (this.username === '') {
                    toast({
                        message: 'Имя пользователя обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                    this.errors.push('Имя пользователя обязательное поле')
                }

                if (this.password === '') {
                    toast({
                        message: 'Пароль обязательное поле',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                    this.errors.push('Пароль обязательное поле')
                }

                if (this.password !== this.password2) {
                    toast({
                        message: 'Пароли должны совпадать',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-right'
                    })
                    this.errors.push('Пароли должны совпадать')
                }

                if (!this.errors.length) {
                    const formData = {
                        username: this.username,
                        password: this.password
                    }

                    axios
                        .post("/api/v1/users/", formData)
                        .then(response => {
                            toast({
                                message: 'Аккаунт был успешно создан',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'top-right'
                            })

                            this.$router.push('/log-in')
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
    }
</script>