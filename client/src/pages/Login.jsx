import React from 'react';
import { Link } from 'react-router-dom';
import { Footer, Navbar } from '../components';
import axios from 'axios';
import { useForm } from 'react-hook-form';

const Login = () => {
  const {
    handleSubmit,
    register,
    formState: { errors },
  } = useForm();
  const submitHandler = async () => {
    console.log('dani');
  };

  return (
    <>
      <Navbar />
      <div className="container my-3 py-3">
        <h1 className="text-center">Login</h1>
        <hr />
        <div class="row my-4 h-100">
          <div className="col-md-4 col-lg-4 col-sm-8 mx-auto">
            <form onSubmit={handleSubmit(submitHandler)}>
              <div class="my-3">
                <label for="display-4">Email address</label>
                <input
                  type="email"
                  class="form-control"
                  id="floatingInput"
                  placeholder="name@example.com"
                  {...register('email', {
                    required: 'Please enter your email',
                    pattern: {
                      value: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/i,
                      message: 'Please enter valid email address',
                    },
                  })}
                />
              </div>
              {errors.email && (
                <div className="text-danger"> {errors.email.message} </div>
              )}
              <div class="my-3">
                <label for="floatingPassword display-4">Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="floatingPassword"
                  placeholder="Password"
                  {...register('password', {
                    required: 'Please enter your password',
                    minLength: {
                      value: 6,
                      message: 'password more than 5 chars',
                    },
                  })}
                />
                {errors.password && (
                  <div className="text-danger">{errors.password.message}</div>
                )}
              </div>
              <div className="my-3">
                <p>
                  New Here?{' '}
                  <Link
                    to="/register"
                    className="text-decoration-underline text-info"
                  >
                    Register
                  </Link>{' '}
                </p>
              </div>
              <div className="text-center">
                <button class="my-2 text-red-400 mx-auto btn btn-dark">
                  Login
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default Login;
