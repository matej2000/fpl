<script setup>
    import axios from 'axios';
    //const axios = require('axios/dist/browser/axios.cjs'); // browser
    var errorMsg = ref(false);
    const route = useRoute()
    if (route.query.e == "1"){
        errorMsg.value = true
    }
    var fixtureData = await sendRequestFixtures("1");
    var generalInfo = await sendRequestGeneralInfo()
    var dictTeamNames = {}
    for(var info of generalInfo.teams){
        dictTeamNames[info.id] = info.short_name
    }
    /* console.log(fixtureData) */
    
    async function getData(id){
        //check if id is valid? check api response status
        if (!isNaN(id)){
            var number = Number(id)
            if (!isNaN(number) && number > 0){
                errorMsg.value = false;
                var a = await navigateTo("/myteam/"+id)
            }
        }
        errorMsg.value = true;
    }

    async function sendRequestFixtures(event){
        try {
            const response = await axios.get("http://localhost:8000/fixtures?event=" + event);
            if(response.status == 200){
                return response.data
            }
            return null;
        } catch (error) {
            return null
        }
    }

    async function sendRequestGeneralInfo(){
        try {
            const response = await axios.get("http://localhost:8000/info");
            if(response.status == 200){
                return response.data
            }
            return null;
        } catch (error) {
            return null
        }
    }

</script>

<template>
    <div role="alert" v-show="errorMsg" class="scroll-smooth">
        <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2">
            Error
        </div>
        <div class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
            <p>Please enter a proper id.</p>
        </div>
    </div>
    <div class="">
        <div class=" bg-[url('/assets/img/cup.jpg')] bg-cover m-auto aspect-video bg-center ">
            <div class="bg-white/40 h-full content-center"> <!-- content-center #align vertically -->
                <div class="test">
                    <div class="font-bold text-[6vmax] md:text-[10vmax] text-pl-secondary w-max flex m-auto leading-none md:leading-tight"> <!-- text-[40px] sm:text-[100px] md:text-[200px] -->
                        <h1>
                            <div class="text-pl-secondary w-max m-auto md:m-0">
                                FPL
                            </div> 
                            <div class="w-max">
                                Assistant
                            </div>
                            <div class=" text-[3vmin] text-right">
                                <a href="#enter_id"><button class="w-full md:w-1/2 mt-3 md:mt-20 bg-transparent hover:bg-pl-secondary text-pl-secondary font-semibold hover:text-white py-2 px-4 border border-pl-secondary hover:border-transparent rounded">
                                    Start
                                </button></a>
                            </div>
                        </h1>
                        <br>
                        
                    </div>
                   <!--  <div class="w-max m-auto">
                        <button  @click="getData(id)" class="mt-3 bg-transparent hover:bg-pl-secondary text-pl-secondary font-semibold hover:text-white py-2 px-4 border border-pl-secondary hover:border-transparent rounded w-[329px] ml-[500px]">
                            Start
                        </button>
                    </div> -->
                </div>
            </div>
        </div>
        <div id="enter_id" class="align-middle bg-pl-secondary break-words">
            <div class="sm:col-span-3 text-center align-baseline pt-20 pb-32">
                <div class="m-auto w-full md:w-1/2">
                <div class="ml-1 mr-1 font-bold text-md md:text-[5vmin] text-white break-word leading-snug">Enter your Fantasy premier league id, to check live rank, leagues and more</div>
                    <div class="mt-10 content-center ">
                        <input v-model="id" type="text" placeholder="Enter your FPL id" name="first-name" id="first-name" class="flex m-auto w-1/2 text-center max-w-md rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                        <button  @click="getData(id)" class="mt-3 bg-white text-pl-secondary font-semibold py-2 px-4 border border-pl-secondary hover:border-transparent rounded">
                            Confirm
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="">
            <div class="mb-4 md:border-2 md:w-[500px]  m-auto md:shadow-2xl p-2 mt-4 ">
                <div class="text-center mt-3 font-bold text-2xl text-pl-secondary">Matchweek 1</div>
                <div v-for="index of fixtureData.length">
                    <div class="flex flex-col w-max m-auto mb-3">
                        <div v-if="index == 1 || fixtureData[index - 1].kickoff_time.split('T')[0] != fixtureData[index - 2].kickoff_time.split('T')[0]" class="text-center mt-5">
                            {{ Date(Date.parse(fixtureData[index - 1].kickoff_time)).split(" ")[0] }}<!-- v-else-if="fixtureData[index].kickoff_time.split('T')[0] != fixtureData[Math.max(1, index-1)].kickoff_time.split('T')[0]" -->
                            {{ Date(Date.parse(fixtureData[index - 1].kickoff_time)).split(" ")[2] }}
                            {{ Date(Date.parse(fixtureData[index - 1].kickoff_time)).split(" ")[1] }}
                        </div>
                        <div class="flex w-max m-auto gap-3 text-center">
                            <div class="h-max m-auto w-12">
                                {{ dictTeamNames[fixtureData[index - 1].team_h] }}
                            </div>
                            <div class="m-auto w-10">
                                <div class="w-10 h-10 bg-cover m-auto" :class="'bg-[url(./assets/img/banners/' + fixtureData[index-1].team_h + '.png)]'"></div>
                            </div>
                            <div class="w-10 m-auto content-center">{{ fixtureData[index - 1].kickoff_time.split('T')[1].substr(0,5) }}</div>
                            <div>
                                <div class="w-10 h-10 bg-cover" :class="'bg-[url(./assets/img/banners/' + fixtureData[index-1].team_a + '.png)]'"></div>
                            </div>
                            <div class="h-max w-10 m-auto">
                                {{ dictTeamNames[fixtureData[index - 1].team_a] }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-if="false" class="bg-[url(./assets/img/banners/1.png)] bg-[url(./assets/img/banners/2.png)] bg-[url(./assets/img/banners/3.png)] bg-[url(./assets/img/banners/4.png)] bg-[url(./assets/img/banners/5.png)]
    bg-[url(./assets/img/banners/6.png)] bg-[url(./assets/img/banners/7.png)] bg-[url(./assets/img/banners/8.png)] bg-[url(./assets/img/banners/9.png)] bg-[url(./assets/img/banners/10.png)] bg-[url(./assets/img/banners/11.png)] bg-[url(./assets/img/banners/12.png)]
    bg-[url(./assets/img/banners/13.png)] bg-[url(./assets/img/banners/14.png)] bg-[url(./assets/img/banners/15.png)] bg-[url(./assets/img/banners/16.png)] bg-[url(./assets/img/banners/17.png)] bg-[url(./assets/img/banners/18.png)] bg-[url(./assets/img/banners/19.png)] bg-[url(./assets/img/banners/20.png)]"></div>
</template>

