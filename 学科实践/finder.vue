<template>
	<view>
		<text>测试临时页</text>
		
        <!-- 条件渲染 -->
				
		<button @click="awesome = !awesome">Toggle</button>
		<h1 v-if="awesome">Vue is awesome!</h1>
		<h1 v-else>Oh no 😢</h1> 

		<block v-if="awesome">
		  <h1>Title</h1>
		  <p>Paragraph 1</p>
		  <p>Paragraph 2</p>
		</block>

		<h1 v-show="ok">Hello!</h1>
		
		<!-- 列表渲染-->
 		<template v-for="(itemmm,indexxx) in itemsss"  :key="indexxx">
			<li  v-if="indexxx<2">
			  	{{ parentMessage }} - {{ indexxx }} - {{ itemmm.message }}
			</li>
		</template>	 
		
		<li v-for="(i,index) in 6">
			{{ i }} --{{index}}
		</li>
		<br>

		<view>
		  <view v-for="value in myObject">
			{{ value }}
		  </view>
		</view>

		<view>
			单向数据绑定：<input type="text" v-bind:value="aname">
			双向数据绑定：<input type="text" v-model:value="aname">
		</view>
			
	</view>
</template>

<script>
	export default {
		data() {
			return {
				ok: false,
				awesome : false,
				parentMessage: 'Parent',
				itemsss: [{ message: 'Foo' }, { message: 'Bar' }, { message: 'Tea' }],
				myObject: {
				      title: 'How to do lists in Vue',
				      author: 'Jane D   oe',
				      publishedAt: '2016-04-10'
				    },
				aname:"Sony",
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
