<script setup lang="ts">
    import {onMounted} from "vue"
    import axios from 'axios';
    
    const route = useRoute()
    var showInfo = false
    var defenders = 3
    var mid= 5
    var attackers = 2
    var managerData = await sendRequest(route.params.id)
    if( Object.is(managerData, null)){
        var a = await navigateTo("/?e=1")
    }
    console.log("JAAAA")
    console.log(managerData)
    

    /*onMounted(()=>{
        var managerData = sendRequest(route.params.id)
        console.log("222222222")
        console.log(managerData)
    })*/

    function press(){
        console.log(sendRequest(route.params.id))
    }

    /*async function sendRequest(id){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://localhost:8000/manager?id="+id)
        xhr.send();
        xhr.responseType = "json"
        xhr.onloadend = () => {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log(xhr.response);
                console.log(xhr.status)
                console.log("ZZZZZZZZZZZZZZZZzzzz")
            } else {
                // redirect back
                console.log(`Error: ${xhr.status}`);
            }
        };
    }*/

    async function sendRequest(id){
        try {
            const response = await axios.get("http://localhost:8000/manager?id="+id);
            return (response.data);
        } catch (error) {
            return null
            //console.error(error);
            //navigateTo()
        }
    }

</script>

<template>
    <div class="container mx-auto mt-20 bg-gray-300">
        <div v-if="managerData">
            <div>
                <h1 class="text-2xl font-bold"> {{ managerData.name}}</h1>
                <h2 class="text-base pl-2">{{ managerData.player_first_name + " " + managerData.player_last_name}} </h2>
            </div>
            <div>
                <div class="grid grid-cols-2 gap-8">
                    <div class="w-1/2">
                        <div class="bg-[url('/assets/img/livefplpitch.svg')] w-fieldw h-fieldh bg-cover bg-center mt-10 ml-10 relative">
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-goal absolute"></div>
                            <!--Defense-->
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-def absolute"></div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-30 top-def absolute"></div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-2 top-def absolute"></div>
                            <div v-if="defenders>3" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-def absolute"></div>
                            <div v-if="defenders>4" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-def absolute"></div>
                            <!--mid-->
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-mid absolute"></div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-30 top-mid absolute"></div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-2 top-mid absolute"></div>
                            <div v-if="mid>3" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-20 top-mid absolute"></div>
                            <div v-if="mid>4" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-20 top-mid absolute"></div>
                            
                        </div>
                    </div>
                    <div class="w-1/2">
                        <h1>Gameweek {{ managerData.current_event }}</h1>
                        <h2>Points</h2>
                        <p>{{ managerData.summary_event_points }}</p>
                        <h2>Overall rank</h2>
                        <p>{{ managerData.summary_overall_rank }}</p>
                    </div>
                
                </div>
            </div>
        </div>
        <div v-else class="">
            <button class="mt-3 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
                    Retry 
            </button>
        </div>
    </div>

</template>