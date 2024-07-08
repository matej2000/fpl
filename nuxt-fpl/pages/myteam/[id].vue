<script setup lang="ts">
    import {onMounted} from "vue"
    import axios from 'axios';
    
    const route = useRoute()
    var showInfo = false
    var gk = []
    var def = []
    var mid = []
    var att= []
    var reserves = []
    var managerData = await sendRequest(route.params.id)
    if (Object.is(managerData, null) || "status_code" in managerData){ //|| "status_code" in manager.value){
        var a = await navigateTo("/?e=1", {external: true})
    }
    else{
        var historyData = await sendRequestHistory(route.params.id)
        var teamData = await sendRequestTeam(route.params.id, managerData.current_event)
        var generalInfo = await sendRequestGeneralInfo()
        var playerPoints = await sendRequestPoints(managerData.current_event)
        for (var x of teamData.picks){
            for (var i of generalInfo.elements){
                if (i.id == x.element){
                    x.first_name = i.first_name
                    x.second_name = i.second_name
                    x.team = i.team
                    x.web_name = i.web_name
                    x.status = i.status
                    x.element_type = i.element_type
                    if (x.element_type == 2 && x.multiplier>0){
                        def.push(x)
                    }else if(x.element_type == 3  && x.multiplier>0){
                        mid.push(x)
                    }else if (x.element_type == 4  && x.multiplier>0){
                        att.push(x)
                    }else if(x.element_type == 1 && x.multiplier>0){
                        gk.push(x)
                    }else{
                        reserves.push(x)
                    }
                    break
                }
            }
            for (var i of playerPoints.elements){
                if (i.id == x.element){
                    x.total_points = i.stats.total_points
                    x.minutes = i.stats.minutes
                    break
                }
            }
            //console.log(x)
        }
        showInfo = true
    }
    
    console.log(def.length, mid.length, att.length, reserves.length)
    console.log(teamData.picks)
    //const {data: manager} = await useFetch("http://localhost:8000/manager?id="+route.params.id)
    //const {data: manager} = await useFetch("https://fantasy.premierleague.com/api/entry/"+route.params.id)

    //console.log("-----------------------------------------------------------")
    //console.log(manager)
    //console.log("-----------------------------------------------------------")
    //console.log(historyData)
    

    /*onMounted(()=>{
        var managerData = sendRequest(route.params.id)
        console.log("222222222")
        console.log(managerData)
    })*/

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
            if(response.status == 200){
                return response.data
            }
            return null;
        } catch (error) {
            return null
        }
    }

    async function sendRequestHistory(id){
        try {
            const response = await axios.get("http://localhost:8000/history?id="+id);
            if(response.status == 200){
                return response.data
            }
            return null;
        } catch (error) {
            return null
        }
    }

    async function sendRequestTeam(id, event){
        try {
            const response = await axios.get("http://localhost:8000/team?id=" + id + "&event=" + event);
            //console.log(response.data)
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

    async function sendRequestPoints(event){
        try {
            const response = await axios.get("http://localhost:8000/points?event=" + event);
            if(response.status == 200){
                return response.data
            }
            return null;
        } catch (error) {
            return null
        }
    }

    function getRowClass(position){
        return "grid-cols-" + position.length
    }
</script>

<template>
    <div v-if="showInfo" class="container mx-auto mt-20 bg-gray-300">
        <div v-if="managerData">
            <div>
                <h1 class="text-2xl font-bold"> {{ managerData.name}}</h1>
                <h2 class="text-base pl-2">{{ managerData.player_first_name + " " + managerData.player_last_name}} </h2>
            </div>
            <div>
                <div class="grid grid-cols-2 gap-8">
                    <div class="w-1/2">
                        <div class="bg-[url('/assets/img/livefplpitch.svg')] w-fieldw h-fieldh bg-cover bg-center mt-10 ml-10 relative">
                            <!--Goalkeeper-->
                            <div class="content-center w-full pt-16"> 
                                <Player :player="gk[0]" :x_position="'m-auto'" :y_position="'top-goal'"/>
                            </div>
                            <!--<div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-goal absolute"></div>-->
                            <!--Defense-->
                            <div :class="getRowClass(def)" class="content-center w-full grid mt-5">
                                <Player v-if="def.length!=4" :player="def[0]" :x_position="'left-40'" :y_position="'top-def'"/>
                                <Player :player="def[1]" :x_position="'left-30'" :y_position="'top-def'"/>
                                <Player :player="def[2]" :x_position="'right-2'" :y_position="'top-def'"/>
                                <Player v-if="def.length>3" :player="def[3]" :x_position="'left-20'" :y_position="'top-def'"/>
                                <Player v-if="def.length>3" :player="def.length==4 ? def[0] : def[4]" :x_position="'right-20'" :y_position="'top-def'"/>
                            </div>
                                <!--<div class="left-40 top-def absolute">
                                <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover"></div>
                                <div class="text-center"><p>Salah</p></div>
                            </div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-30 top-def absolute"></div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-2 top-def absolute"></div>
                            <div v-if="def.length>3" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-20 top-def absolute"></div>
                            <div v-if="def.length>4" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-20 top-def absolute"></div>-->
                            <!--mid-->
                            <div class="content-center w-full grid mt-5" :class="getRowClass(mid)">
                                <Player v-if="mid.length!=4" :player="mid[0]" :x_position="'left-40'" :y_position="'top-mid'"/>
                                <Player :player="mid[1]" :x_position="'left-30'" :y_position="'top-mid'"/>
                                <Player :player="mid[2]" :x_position="'right-2'" :y_position="'top-mid'"/>
                                <Player v-if="mid.length>3" :player="mid[3]" :x_position="'left-20'" :y_position="'top-mid'"/>
                                <Player v-if="mid.length>3" :player="mid.length==4 ? mid[0] : mid[4]" :x_position="'right-20'" :y_position="'top-mid'"/>
                            </div>
                                <!--
                            <div v-if="mid.length!=4" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-mid absolute"></div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-30 top-mid absolute"></div>
                            <div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-2 top-mid absolute"></div>
                            <div v-if="mid.length>3" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-20 top-mid absolute"></div>
                            <div v-if="mid.length>3" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-20 top-mid absolute"></div>
                            -->
                            <!--Attack-->
                            <div class="content-center w-full grid mt-5" :class="getRowClass(att)">
                                <Player :player="att[0]"/>
                                <Player v-if="att.length>1" :player="att[1]"/>
                                <Player v-if="att.length>2" :player="att[2]"/>
                            </div>
                            <!--<div v-if="att.length==1 || att.length ==3" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-att absolute"></div>
                            <div v-if="att.length>1" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-30 top-att absolute"></div>
                            <div v-if="att.length>1" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-2 top-att absolute"></div>-->
                            <!--Reserves-->
                            <div class="content-center w-full grid mt-10 grid-cols-4 bg-gray-200 pt-4 pb-4">
                                <PlayerPosition v-for="r in reserves" :player="r"/>
                            </div>
                        </div>
                    </div>
                    <div class="w-1/2">
                        <h1>Gameweek {{ managerData.current_event }}</h1>
                        <h2>Points</h2>
                        <p>{{ managerData.summary_event_points }}</p>
                        <h2>Overall rank</h2>
                        <p>{{ managerData.summary_overall_rank }}</p>
                        <div>
                            <ul>
                                <li v-for="league in managerData.leagues.classic">{{ league.name }} {{ league.entry_rank }}</li>
                            </ul>
                        </div>
                    </div>
                
                </div>
            </div>
        </div>
        <div v-else class="grid-cols-5 grid-cols-4 grid-cols-3 grid-cols-2"><!--For some reason dynamically assigning some tailwind classes with vue js does not import them, this somehow works-->
            <button class="mt-3 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
                    Retry 
            </button>
        </div>
    </div>

</template>