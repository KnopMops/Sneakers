<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Спасибо</h1>
                <p>Ваш заказ будет доставлен вам в течении 48 часов</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Success',
        mounted() {
            document.title = 'Спасибо, что выбрали нас | Sneakers'
        }
    }
</script>