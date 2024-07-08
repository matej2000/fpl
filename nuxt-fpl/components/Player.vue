<template>
    <div class="w-max m-auto">
      <div class="grid w-max"><!-- grid-rows-2 -->
          <div class="w-20 h-20 bg-cover" :class="team_path" :id="player.position">
            <svg v-if="player.is_captain" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" focusable="false" class="text-white"><title>Captain</title><circle cx="12" cy="12" r="12" aria-hidden="true"></circle><path d="M15.0769667,14.370341 C14.4472145,15.2780796 13.4066319,15.8124328 12.3019667,15.795341 C10.4380057,15.795341 8.92696674,14.284302 8.92696674,12.420341 C8.92696674,10.55638 10.4380057,9.045341 12.3019667,9.045341 C13.3988206,9.06061696 14.42546,9.58781014 15.0769667,10.470341 L17.2519667,8.295341 C15.3643505,6.02401882 12.1615491,5.35094208 9.51934028,6.67031017 C6.87713147,7.98967826 5.49079334,10.954309 6.17225952,13.8279136 C6.8537257,16.7015182 9.42367333,18.7279285 12.3769667,18.720341 C14.2708124,18.7262708 16.0646133,17.8707658 17.2519667,16.395341 L15.0769667,14.370341 Z" fill="currentColor" aria-hidden="true"></path></svg>
            <svg v-if="player.is_vice_captain" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" focusable="false" class="text-white"><title>Captain</title><circle cx="12" cy="12" r="12" aria-hidden="true"></circle><polygon points="13.5 .375 8.925 12.375 4.65 12.375 0 .375 3.15 .375 6.75 10.05 10.35 .375" transform="translate(5.25 6)" fill="currentColor" aria-hidden="true"></polygon></svg>
          </div>
          <div class="text-cente grid grid-rows-2">
            <div v-if="player.status == 'i'" class="text-center bg-red-500 text-white px-1"><p>{{player.web_name}}</p></div>
            <div v-else-if="player.status == 'd'" class="text-center bg-orange-500 text-white px-1"><p>{{player.web_name}}</p></div>
            <div v-else class="text-center bg-black text-white px-1"><p>{{player.web_name}}</p></div>
            <div class="text-center bg-white"><p>{{ player.total_points }}</p></div>
          </div>
      </div>
  </div>
  <!--<div v-if="false" class="bg-[url('/assets/img/1.png')] bg-[url('/assets/img/2.png')] bg-[url('/assets/img/3.png')] bg-[url('/assets/img/4.png')] bg-[url('/assets/img/5.png')]
                           bg-[url('/assets/img/6.png')] bg-[url('/assets/img/7.png')] bg-[url('/assets/img/8.png')] bg-[url('/assets/img/9.png')] bg-[url('/assets/img/10.png')]
                           bg-[url('/assets/img/11.png')] bg-[url('/assets/img/12.png')] bg-[url('/assets/img/13.png')] bg-[url('/assets/img/14.png')] bg-[url('/assets/img/15.png')]
                           bg-[url('/assets/img/16.png')] bg-[url('/assets/img/17.png')] bg-[url('/assets/img/18.png')] bg-[url('/assets/img/19.png')] bg-[url('/assets/img/20.png')]"></div>
-->
</template>

<script setup>
const props = defineProps({
  player: {
    type: Object,
    required: true,
  },
});
const {player} = props;
const team_path = "bg-[url('/assets/img/" + player.team + ".png')]"
</script>