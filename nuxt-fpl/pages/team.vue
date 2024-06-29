<script setup>
    function getParam(){
        console.log($route.query)
    }
</script>

<template>
    Your team.
    <button @click="getParam">Dela</button>
</template>