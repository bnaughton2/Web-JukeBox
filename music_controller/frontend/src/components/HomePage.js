import React, { Component } from "react";
import RoomJoinPage from './RoomJoinPage'
import CreateRoomPage from './CreateRoomPage'
import Room from './Room'
import { BrowserRouter as Router, Routes, Link, Route, Redirect } from "react-router-dom";

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return <Router>
            <Routes>
                <Route path='/' element={<p>Homepage</p>}></Route>
                <Route path='/join' element={<RoomJoinPage />}></Route>
                <Route path='/create' element={<CreateRoomPage />}></Route>
                <Route path='/room/:roomCode' element={<Room />}></Route>
            </Routes>
        </Router>
    }
}