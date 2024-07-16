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
    var gameweek_stats = [0, 0, 0, 0, 0, 0]
    var current_event_data = {"average_entry_score":1}
    var managerData = await sendRequest(route.params.id)
    if (Object.is(managerData, null) || "status_code" in managerData){ //|| "status_code" in manager.value){
        var a = await navigateTo("/?e=1", {external: true})
    }
    else{
        var teamData = await sendRequestTeam(route.params.id, managerData.current_event)
        var generalInfo = await sendRequestGeneralInfo()
        var playerPoints = await sendRequestPoints(managerData.current_event)
        var fixtures = await sendRequestFixtures(managerData.current_event)
        var dictTeamNames = {}
        current_event_data = generalInfo.events[managerData.current_event-1]
        for(var info of generalInfo.teams){
            dictTeamNames[info.id] = info.short_name
        }
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
                    x.explain_points = i.explain
                    for (var explain of x.explain_points){
                        for (var fixture of fixtures){
                            if(explain.fixture == fixture.id){
                                explain.team_h = dictTeamNames[fixture.team_h]
                                explain.team_h_score = fixture.team_h_score
                                explain.team_a_score = fixture.team_a_score
                                explain.team_a = dictTeamNames[fixture.team_a]
                                break
                            }
                        }
                        for (var stat of explain.stats){
                            if (stat.identifier == "goals_scored"){
                                gameweek_stats[0] += stat.value
                            }
                            else if (stat.identifier == "assists"){
                                gameweek_stats[1] += stat.value
                            }
                            else if (stat.identifier == "clean_sheets"){
                                gameweek_stats[2] += stat.value
                            }
                            else if (stat.identifier == "bonus"){
                                gameweek_stats[3] += stat.value
                            }
                            else if (stat.identifier == "yellow_cards"){
                                gameweek_stats[4] += stat.value
                            }
                            else if (stat.identifier == "red_cards"){
                                gameweek_stats[5] += stat.value
                            }
                        }
                    }
                    break
                }
            }
            console.log(x.explain_points[0].stats)
            
        }
        showInfo = true
    }
    
    console.log(def.length, mid.length, att.length, reserves.length)
    console.log(gameweek_stats)
    //console.log(managerData)
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

    function getRowClass(position){
        return "grid-cols-" + position.length
    }
</script>

<template>
    <div v-if="showInfo" class="container mx-auto mt-20 ">
        <div v-if="managerData" class="max-w-[1300px] m-auto">
            <div>
                <h1 class="text-2xl font-bold"> {{ managerData.name}}</h1>
                <h2 class="text-base pl-2">{{ managerData.player_first_name + " " + managerData.player_last_name}} </h2>
            </div>
            <div>
                <div class="grid grid-cols-3 gap-8 ">
                    <div class="border-solid col-span-3 md:col-span-2 rounded-xl shadow-2xl bg-gradient-to-r from-pl-primary to-pl-third overflow-hidden">
<!--                         <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
 -->                        <div>
                            <div class="">
                                <div class="m-auto text-center w-max"><h1 class="font-bold">Gameweek {{ managerData.current_event }}</h1></div>
                                <div class="grid grid-cols-3 text-center">
                                    <div class="pt-6">
                                        <div class="text-sm sm:text-base"><p>Average points</p></div>
                                        <div class="text-2xl"><p>{{ current_event_data.average_entry_score }}</p></div>
                                    </div>
                                    <div class="p-4 text-white rounded bg-pl-secondary">
                                        <div class="text-sm sm:text-base"><p>Final points</p></div>
                                        <div class="text-5xl"><p>{{ managerData.summary_event_points }}</p></div>
                                    </div>
                                    <div class="pt-6">
                                        <div class="text-sm sm:text-base"><p>Highest points</p></div>
                                        <div class="text-2xl"><p>{{ current_event_data.highest_score }}</p></div>
                                    </div>

                                </div>
                            </div>
                            <div class="bg-[url('/assets/img/fpl_pitch.svg')] bg-cover bg-top mt-10 m-auto rounded-xl">
                                <div class="max-w-[800px] m-auto pt-5">
                                    <!--Goalkeeper-->
                                    <div class="content-center w-full"> 
                                        <Player :player="gk[0]" :x_position="'m-auto'" :y_position="'top-goal'"/>
                                    </div>
                                    <!--<div class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-goal absolute"></div>-->
                                    <!--Defense-->
                                    <div :class="getRowClass(def)" class="content-center w-full grid mt-5">
                                        <Player v-for="r in def" :player="r"></Player>
                                        <!-- <Player v-if="def.length!=4" :player="def[0]" :x_position="'left-40'" :y_position="'top-def'"/>
                                        <Player :player="def[1]" :x_position="'left-30'" :y_position="'top-def'"/>
                                        <Player :player="def[2]" :x_position="'right-2'" :y_position="'top-def'"/>
                                        <Player v-if="def.length>3" :player="def[3]" :x_position="'left-20'" :y_position="'top-def'"/>
                                        <Player v-if="def.length>3" :player="def.length==4 ? def[0] : def[4]" :x_position="'right-20'" :y_position="'top-def'"/> -->
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
                                        <Player v-for="r in mid" :player="r"></Player>
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
                                        <Player v-for="r in att" :player="r"></Player>
                                    </div>
                                    <!--<div v-if="att.length==1 || att.length ==3" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-40 top-att absolute"></div>
                                    <div v-if="att.length>1" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover left-30 top-att absolute"></div>
                                    <div v-if="att.length>1" class="bg-[url('/assets/img/player_test.png')] w-20 h-20 bg-cover right-2 top-att absolute"></div>-->
                                    <!--Reserves-->
                                    <div class="content-center w-full grid mt-10 grid-cols-4 bg-gray-200 m-auto rounded-t-xl pt-4 pb-4 bg-opacity-50 -p-10 max-w-[800px]">
                                        <PlayerPosition v-for="r in reserves" :player="r"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="w-full col-span-3 md:col-span-1 mx-auto">
                        <div class="text-base rounded-xl shadow-xl">
                            <div class="text-center py-1 rounded-t-xl bg-pl-secondary text-white"><h1>Gameweek stats</h1></div>
                            <div class="px-3 pb-2">
                                <ul>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Goals scored</h5><div class="">{{ gameweek_stats[0] }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Assists</h5><div class="">{{ gameweek_stats[1] }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Clean sheets</h5><div class="">{{ gameweek_stats[2] }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Bonus points</h5><div class="">{{ gameweek_stats[2] }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Yellow cards</h5><div class="">{{ gameweek_stats[3] }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2"><h5>Red cards</h5><div class="">{{ gameweek_stats[4] }}</div></div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="text-base rounded-xl shadow-xl mt-10">
                            <div class="text-center py-1 rounded-t-xl bg-pl-secondary text-white"><h1>{{ managerData.player_first_name }} {{ managerData.player_last_name }}</h1></div>
                            <div class="px-3 pb-2">
                                <ul>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Overall points</h5><div class="">{{ managerData.summary_overall_points }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Overall rank</h5><div class="">{{ managerData.summary_overall_rank }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2 border-b-2"><h5>Gameweek points</h5><div class="">{{ managerData.summary_event_points }}</div></div>
                                    </li>
                                    <li>
                                        <div class="flex justify-between pt-2"><h5>Gameweek rank</h5><div class="">{{ managerData.summary_event_rank }}</div></div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="bg-white mt-10 mb-10 rounded-xl shadow-xl ">
                            <div class="text-center bg-pl-secondary py-2 rounded-t-xl text-white">Leagues</div>
                            <div class="px-3 pb-2">
                                <ul>
                                    <li v-for="index in 4">
                                        <div v-if="index != 4" class="flex justify-between pt-2 border-b-2"><div>{{ managerData.leagues.classic[index].name }}</div> <div class="">{{ managerData.leagues.classic[index].entry_rank }}</div></div>
                                        <div v-else class="flex justify-between pt-2"><div>{{ managerData.leagues.classic[index].name }}</div> <div class="">{{ managerData.leagues.classic[index].entry_rank }}</div></div>
                                    </li>
                                </ul>
                            </div>
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