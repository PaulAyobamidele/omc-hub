import { useState } from 'react'
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        username: '',
        password: ''
    })

    const handleLoginChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleLoginSubmit = (e) => {
        e.preventDefault(); // Prevent form submission
        
        fetch('http://127.0.0.1:8000/auth/login/', {
            method: "POST",
            headers: { 'content-Type': 'application/json' },
            body: JSON.stringify(formData)
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.token) {
                localStorage.setItem('token', data.token)
                navigate('/')
            } else {
                console.error('There is an error: ', data.error)
            }
        })
        .catch((error) => {
            console.error('Error: ', error);
        });
    }

    return (
        <div className="login__container">
            <h2>Login</h2>
            <form onSubmit={handleLoginSubmit}>
                <div>
                    <label htmlFor="username">
                        Username:
                    </label>
                    <input
                        type="text"
                        id='username'
                        name='username'
                        value={formData.username}
                        onChange={handleLoginChange}
                        required
                    />
                </div>

                <div>
                    <label htmlFor="password">
                        Password:
                    </label>
                    <input
                        type="password" 
                        id='password'
                        name='password'
                        value={formData.password}
                        onChange={handleLoginChange}
                        required
                    />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    )
}

export default Login
