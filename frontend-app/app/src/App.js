import React, { Component } from 'react';
import { Row, Col } from 'antd';
import Logo from './assets/logo.png';

class App extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div style={{ height: '100%' }}>
			<Row style={{ width: '100%', height: 75 }}>
				<div style={{ margin: 10 }}>
				<img src={Logo} style={{ height: 30 }}/>

				</div>
			</Row>
			<Row style={{ width: '100%' }}>
				<Col span={4}/>
				<Col span={16}>

				</Col>
				<Col span={4}/>
			</Row>
			</div>
		)
	}
}

export default App;