<script setup>
    //const axios = require('axios/dist/browser/axios.cjs'); // browser
    var errorMsg = ref(false);
    const route = useRoute()
    if (route.query.e == "1"){
        errorMsg.value = true
    }
    
    async function getData(id){
        //check if id is valid? check api response status
        if (!isNaN(id)){
            console.log(id)
            var number = Number(id)
            if (!isNaN(number) && number > 0){
                errorMsg.value = false;
                var a = await navigateTo("/myteam/"+id)
                return;
            }
        }
        errorMsg.value = true;
    }

</script>

<template>
    <div role="alert" v-show="errorMsg">
        <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2">
            Error
        </div>
        <div class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
            <p>Please enter a proper id.</p>
        </div>
    </div>
    <div class="bg-gray-500 w-full ">
    <div class="align-middle">
        <div class="sm:col-span-3 text-center align-baseline pt-32 pb-32">
          <label for="first-name" class="block text-md ml-1 mr-1 font-medium leading-6 text-gray-900">Enter your Fantasy premier league id, to check live rank, leagues and more</label>
            <div class="mt-10 content-center">
                <input v-model="id" type="text" placeholder="Enter your FPL id" name="first-name" id="first-name" class="block m-auto w-full text-center max-w-sm rounded-md pl-3 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                <button  @click="getData(id)" class="mt-3 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
                    Confirm
                </button>
            </div>
        </div>
    </div>
    </div>
</template>

