import {useState} from 'react'

const Registration = () => {

  const [formData, setFormData] = useState({
    username : '',
    email : '',
    password: ''
    })

    const handleChange = (e) => {
      setFormData({ ...formData, [e.target.name] : e.target.value })
    }

    const handleSubmit = () => {
      fetch('http://127.0.0.1:8000/registration/register/', {
        method: 'POST',
        headers: {'content-Type': 'application/json'},
        body: JSON.stringify(formData)
      })
      .then((res) => {res.json()})
      .then((data) => {console.log(data)})
      .catch((error) => {console.error('Error', error)})
    }
  return (
    <div className="registration__container">
      <h2>Registration Form</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">
            <input 
              type="text"
              id = 'username'
              name = 'username'
              value = {formData.username}
              onChange = {handleChange}
              required />
          </label>
        </div>

        <div>
          <label htmlFor="email">
            <input 
              type="text"
              id = 'email'
              name = 'email'
              value = {formData.email}
              onChange = {handleChange}
              required />
          </label>
        </div>


        <div>
          <label htmlFor="password">
            <input 
              type="text"
              id = 'password'
              name = 'password'
              value = {formData.password}
              onChange = {handleChange}
              required />
          </label>
        </div>
        <button type='submit'>Submit</button>
      </form>
    </div>
  )
}

export default Registration
